
import requests
import psutil

url = "http://localhost:11434/api/generate"

data = {
    "model": "qwen2.5:1.5b",
    "prompt": "What is AI?",
    "stream": False,
"options": {"num_ctx": 8192}}

response = requests.post(url, json=data)

memory = 0

for p in psutil.process_iter(["name", "memory_info"]):
    if p.info["name"] and "ollama" in p.info["name"].lower():
        memory += p.info["memory_info"].rss

print("Ollama Memory:", round(memory / (1024 * 1024), 2), "MB")
