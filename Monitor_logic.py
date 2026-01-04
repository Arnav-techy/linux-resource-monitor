

import psutil
import time
import os
from datetime import datetime

prev=(psutil.net_io_counters(), time.time())


def _human_rate(bps):
    if bps >= 1024**2:
        return f"{bps/1024**2:.2f} MB/s"
    if bps >= 1024:
        return f"{bps/1024:.2f} KB/s"
    return f"{bps:.0f} B/s"


def get_resource_usage(prev):
    prev_io, prev_ts = prev
    print("="*60)
    print("           LINUX RESOURCE MONITOR")
    print("="*60)
    cpu_usage=psutil.cpu_percent(interval=1)
    cpu_usage_core = psutil.cpu_percent(percpu=True)
    cpu_core=psutil.cpu_count(logical=False)
    cpu_cores=psutil.cpu_count(logical=True)
    memory=psutil.virtual_memory()
    disk=psutil.disk_usage('/')
    curr=psutil.net_io_counters()
    curr_ts = time.time()
    elapsed = curr_ts - prev_ts if curr_ts - prev_ts > 0 else 1

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Timestamp:          {timestamp}")
    print("CPU Usage:")
    print("-"*60)
    print(f"  Overall:          {cpu_usage}%")
    print(f"  Per Core:         {cpu_usage_core}%")
    print(f"  Physical Cores:   {cpu_core}")
    print(f"  Logical Cores:    {cpu_cores}")
    print("Memory Usage:")
    print("-"*60)
    print(f"  Total:            {memory.total/1024**3:.2f} GB")
    print(f"  Available:        {memory.available/1024**3:.2f} GB")
    print(f"  Used:             {memory.used/1024**3:.2f} GB")
    print(f"  Percentage:       {memory.percent}%")
    print("Disk Usage:")
    print("-"*60)
    print(f"  Total:            {disk.total/1024**3:.2f} GB")
    print(f"  Used:             {disk.used/1024**3:.2f} GB")
    print(f"  Free:             {disk.free/1024**3:.2f} GB")
    print("Network I/O:")
    print("-"*60)
    if curr:
        sent_delta = curr.bytes_sent - prev_io.bytes_sent
        recv_delta = curr.bytes_recv - prev_io.bytes_recv
        sent_per_sec = sent_delta / elapsed
        recv_per_sec = recv_delta / elapsed
        print(f"  Overall Bytes Sent:       {curr.bytes_sent}")
        print(f"  Overall Bytes Received:   {curr.bytes_recv}")
        print(f"  Sent/second:              {sent_delta} bytes over {elapsed:.1f}s ({_human_rate(sent_per_sec)})")
        print(f"  Received/second:          {recv_delta} bytes over {elapsed:.1f}s ({_human_rate(recv_per_sec)})")

    return (curr, curr_ts)

    
try:  
    while True:
        os.system('clear')
        prev=get_resource_usage(prev)
        time.sleep(20)

except KeyboardInterrupt:
    os.system('clear')
    print("Linux resource monitor has stopped. Goodbye")
