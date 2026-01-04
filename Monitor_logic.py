
import psutil
import time
import os
from datetime import datetime

print("LINUX RESOURCE MONITOR")
def get_resource_usage():
    cpu_usage=psutil.cpu_percent(interval=1)
    cpu_usage_core=psutil.cpu_percent(interval=1, logical=False)
    memory=psutil.virtual_memory()
    disk=psutil.disk_usage('/')
    net_io=psutil.net_io_counters()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("CPU Usage:")
    print(f"  Overall: {cpu_usage}%")
    print(f"  Per Core: {cpu_usage_core}%")
    print("Memory Usage:")
    print(f"  Total: {memory.total/1024**3:.2f} GB")
    print(f"  Available: {memory.available/1024**3:.2f} GB")
    print(f"  Used: {memory.used/1024**3:.2f} GB")
    print(f"  Percentage: {memory.percent}%")
    print("Disk Usage:")
    print(f"  Total: {disk.total/1024**3:.2f} GB")
    print(f"  Used: {disk.used/1024**3:.2f} GB")
    print(f"  Free: {disk.free/1024**3:.2f} GB")
    print("Network I/O:")
    if net_io:
        print(f"  Bytes Sent: {net_io.bytes_sent}")
        print(f"  Bytes Received: {net_io.bytes_recv}")