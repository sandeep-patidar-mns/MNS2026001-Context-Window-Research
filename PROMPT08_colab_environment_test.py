# Prompt 08: Colab diagnostic. Run this cell in Google Colab and share the ACTUAL output.
# This does not download a model or dataset.
import sys, platform, importlib.util, os
print("python_version:", sys.version.split()[0])
print("platform:", platform.platform())
try:
    import torch
    print("torch_version:", torch.__version__)
    print("torch_cuda_build:", torch.version.cuda)
    print("cuda_available:", torch.cuda.is_available())
    print("gpu_count:", torch.cuda.device_count())
    if torch.cuda.is_available():
        for i in range(torch.cuda.device_count()):
            p = torch.cuda.get_device_properties(i)
            print(f"gpu_{i}_name:", p.name)
            print(f"gpu_{i}_total_memory_gib:", round(p.total_memory / (1024**3), 2))
            x = torch.ones((512, 512), device=f"cuda:{i}")
            y = x @ x
            torch.cuda.synchronize()
            print(f"gpu_{i}_sanity_matmul:", tuple(y.shape), "finite:", bool(torch.isfinite(y).all().item()))
    else:
        print("gpu_sanity_test: SKIPPED (CUDA unavailable)")
except Exception as e:
    print("torch_diagnostic_error:", type(e).__name__, str(e))
for package in ["transformers", "datasets", "accelerate", "bitsandbytes", "sentence_transformers"]:
    print(f"{package}_installed:", importlib.util.find_spec(package) is not None)
print("diagnostic_complete: true")
