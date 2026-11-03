
# AI Engineering Project
# Final Profiling Results

results = [
    {
        "context": 1024,
        "ttft": 41.784,
        "tokens": 50,
        "latency": 0.0934,
        "memory": 1031.79,
        "vram": 0.0
    },
    {
        "context": 2048,
        "ttft": 12.497,
        "tokens": 50,
        "latency": 0.0930,
        "memory": 1060.79,
        "vram": 0.0
    },
    {
        "context": 4096,
        "ttft": 7.133,
        "tokens": 50,
        "latency": 0.0945,
        "memory": 1118.79,
        "vram": 0.0
    },
    {
        "context": 8192,
        "ttft": 8.779,
        "tokens": 50,
        "latency": 0.0927,
        "memory": 1310.31,
        "vram": 0.0
    }
]

print("=" * 85)
print("       LOCAL MODEL INFERENCE - FINAL RESULTS")
print("=" * 85)

print(
    f"{'Context':<12}"
    f"{'TTFT (s)':<14}"
    f"{'Tokens':<12}"
    f"{'Latency (s)':<15}"
    f"{'Memory (MB)':<16}"
    f"{'VRAM (MB)':<12}"
)

print("-" * 85)

for r in results:
    print(
        f"{r['context']:<12}"
        f"{r['ttft']:<14.3f}"
        f"{r['tokens']:<12}"
        f"{r['latency']:<15.4f}"
        f"{r['memory']:<16.2f}"
        f"{r['vram']:<12.2f}"
    )

print("-" * 85)
print("Profiling results displayed successfully.")
