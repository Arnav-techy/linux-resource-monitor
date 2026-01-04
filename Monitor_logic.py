

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

    def _fmt_bytes(n):
        # human friendly bytes for totals
        if n >= 1024**3:
            return f"{n/1024**3:.2f} GB"
        if n >= 1024**2:
            return f"{n/1024**2:.2f} MB"
        if n >= 1024:
            return f"{n/1024:.2f} KB"
        return f"{n} B"

    def _line(label, value):
        LABEL_W = 24
        print(f"  {label:<{LABEL_W}} {value}")

    print("="*60)
    print("           LINUX RESOURCE MONITOR")
    print("="*60)

    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_usage_core = psutil.cpu_percent(percpu=True)
    cpu_core = psutil.cpu_count(logical=False)
    cpu_cores = psutil.cpu_count(logical=True)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    curr = psutil.net_io_counters()
    curr_ts = time.time()
    elapsed = curr_ts - prev_ts if curr_ts - prev_ts > 0 else 1

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    _line('Timestamp:', timestamp)

    print('\nCPU Usage:')
    print('-'*60)
    _line('Overall:', f"{cpu_usage:.1f}%")
    # per-core on separate aligned lines
    for i, pct in enumerate(cpu_usage_core):
        _line(f'Core {i}:', f"{pct:.1f}%")
    _line('Physical Cores:', cpu_core)
    _line('Logical Cores:', cpu_cores)

    print('\nMemory Usage:')
    print('-'*60)
    _line('Total:', _fmt_bytes(memory.total))
    _line('Available:', _fmt_bytes(memory.available))
    _line('Used:', _fmt_bytes(memory.used))
    _line('Percentage:', f"{memory.percent}%")

    print('\nDisk Usage:')
    print('-'*60)
    _line('Total:', _fmt_bytes(disk.total))
    _line('Used:', _fmt_bytes(disk.used))
    _line('Free:', _fmt_bytes(disk.free))

    print('\nNetwork I/O:')
    print('-'*60)
    if curr:
        sent_delta = curr.bytes_sent - prev_io.bytes_sent
        recv_delta = curr.bytes_recv - prev_io.bytes_recv
        sent_per_sec = sent_delta / elapsed
        recv_per_sec = recv_delta / elapsed
        _line('Overall Bytes Sent:', _fmt_bytes(curr.bytes_sent))
        _line('Overall Bytes Recv:', _fmt_bytes(curr.bytes_recv))
        _line('Sent (delta):', f"{sent_delta} bytes over {elapsed:.1f}s ({_human_rate(sent_per_sec)})")
        _line('Recv (delta):', f"{recv_delta} bytes over {elapsed:.1f}s ({_human_rate(recv_per_sec)})")

    return (curr, curr_ts)

    
try:  
    while True:
        os.system('clear')
        prev=get_resource_usage(prev)
        time.sleep(20)

except KeyboardInterrupt:
    os.system('clear')
    print("Linux resource monitor has stopped. Goodbye")
