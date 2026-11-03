import requests
import time
import json

url = "http://localhost:11434/api/generate"
ps_url = "http://localhost:11434/api/ps"

model = "qwen2.5:1.5b"
context_sizes = [1024, 2048, 4096, 8192]

print("AI Model Hardware Profiler")
print("-" * 65)

for context in context_sizes:

    print(f"\nContext Size: {context}")

    data = {
        "model": model,
        "prompt": "Explain Artificial Intelligence.",
        "stream": True,
        "options": {
            "num_ctx": context,
            "num_predict": 50
        }
    }

    start = time.perf_counter()
    ttft = None
    final_result = {}

    response = requests.post(url, json=data, stream=True)
    response.raise_for_status()

    for line in response.iter_lines():
        if line:
            result = json.loads(line)

            if result.get("response") and ttft is None:
                ttft = time.perf_counter() - start

            if result.get("done"):
                final_result = result

    # Actual token measurements
    token_count = final_result.get("eval_count", 0)
    eval_duration = final_result.get("eval_duration", 0)

    generation_time = eval_duration / 1_000_000_000

    if token_count > 0:
        latency = generation_time / token_count
    else:
        latency = 0

    # Memory measurements from Ollama
    ps_response = requests.get(ps_url)
    ps_response.raise_for_status()

    models = ps_response.json().get("models", [])

    model_memory = 0
    vram_memory = 0

    for item in models:
        if item.get("name") == model:
            model_memory = item.get("size", 0) / (1024 * 1024)
            vram_memory = item.get("size_vram", 0) / (1024 * 1024)
            break

    print("TTFT:", round(ttft or 0, 3), "seconds")
    print("Actual Tokens:", token_count)
    print("Inter-token Latency:", round(latency, 4), "seconds")
    print("Model Memory:", round(model_memory, 2), "MB")
    print("VRAM Usage:", round(vram_memory, 2), "MB")

print("\nProfiling Completed.")
