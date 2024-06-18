import torch
from memory_profiler import memory_usage
from ultralytics import YOLO

device = "cuda" if torch.cuda.is_available() else "cpu"
source = '/home/frame446.jpg'

# Function to measure memory and run inference
def measure_memory_and_time():
    # Add necessary imports, variables, or setups here if any
    start_time = time.time()
    model = YOLO("/home/int8/yolov8s_int8.engine", task="detect")
    results = model.predict(source, device=device)
    end_time = time.time()
    inference_time = end_time - start_time
    print(f"Inference Time: {inference_time} seconds")
    return results, inference_time

# Measure initial memory usage (assumes memory_usage function is imported)
initial_memory = memory_usage(-1, interval=0.05, timeout=1)

# Run the function and measure memory during execution
mem_usage = memory_usage(
    (measure_memory_and_time, (), {}), 
    interval=0.05, 
    include_children=True,
    max_usage=False,
    retval=False
)

# Measure final peak memory usage
final_peak_memory = max(mem_usage)

# Calculate average memory usage
average_memory = sum(mem_usage) / len(mem_usage)

print(f"Peak Memory Usage: {final_peak_memory} MiB")
print(f"Average Memory Usage: {average_memory} MiB")
