# AI Engineering Project

## Project Title
Local Model Inference & Hardware Profiler

## Project Description
This project runs an open-source Large Language Model locally using Ollama and evaluates its inference performance under different context sizes.

## Model Used
- Qwen 2.5 – 1.5B
- Runtime: Ollama
- Model size selected due to hardware limitations.

## Performance Metrics
1. **Time To First Token (TTFT):** Measures the time from sending the request until the first generated text is received.
2. **Inter-token Generation Latency:** Calculates average generation time per actual output token using Ollama's `eval_count` and `eval_duration`.
3. **Memory Scaling:** Measures the model memory reported by Ollama at different context sizes.
4. **VRAM Usage:** Reports GPU memory usage when available.

## Experimental Setup
Context sizes tested:
- 1024 tokens
- 2048 tokens
- 4096 tokens
- 8192 tokens

The model generates up to 50 tokens for each test.

## Results

| Context Size | TTFT (sec) | Actual Tokens | Latency (sec/token) | Model Memory (MB) | VRAM (MB) |
|---|---:|---:|---:|---:|---:|
| 1024 | 41.784 | 50 | 0.0934 | 1031.79 | 0 |
| 2048 | 12.497 | 50 | 0.0930 | 1060.79 | 0 |
| 4096 | 7.133 | 50 | 0.0945 | 1118.79 | 0 |
| 8192 | 8.779 | 50 | 0.0927 | 1310.31 | 0 |

## Hardware Limitation
The model runs on CPU because the computer does not have a dedicated GPU. Therefore, VRAM usage is reported as 0 MB. Model memory values are reported by Ollama and should not be interpreted as exact GPU or total system RAM usage.

## Tools & Libraries
- Python
- Ollama
- Requests
- JSON

## Main File
`profiler.py` – Runs the model and measures TTFT, average per-token generation latency, model memory, and VRAM usage.
