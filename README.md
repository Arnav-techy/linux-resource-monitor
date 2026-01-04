## LINUX RESOURCE MONITOR

This is a command-line based Linux resource monitoring tool written in Python.
It displays system statistics such as CPU usage, memory usage, disk usage, and network activity in a structured and readable format.

The project was built to understand how Linux system resources can be accessed and monitored programmatically using Python.

What This Program Shows

The monitor displays the following information:

CPU

1. Overall CPU usage percentage

2. Per-core CPU usage

3. Number of physical CPU cores

4. Number of logical CPU cores

Memory

1. Total system memory

2. Available memory

3. Used memory

4. Memory usage percentage

Disk

1. Total disk space (root filesystem /)

2. Used disk space

3. Free disk space

Network

1. Total bytes sent since system start

2. Total bytes received since system start

3. Upload speed (bytes per second)

4. Download speed (bytes per second)

All values refresh automatically at a fixed interval.

## Sample Output

```
============================================================
                 LINUX RESOURCE MONITOR
============================================================
Timestamp              : 2026-01-05 03:57:20

CPU USAGE
------------------------------------------------------------
Overall Usage          : 0.8 %
Per Core Usage         
  Core 0               : 3.0 %
  Core 1               : 2.9 %
  Core 2               : 2.0 %
  Core 3               : 1.7 %
Physical Cores         : 2
Logical Cores          : 4

MEMORY USAGE
------------------------------------------------------------
Total                  : 7.70 GB
Available              : 5.88 GB
Used                   : 1.82 GB
Usage Percentage       : 23.7 %

DISK USAGE
------------------------------------------------------------
Total                  : 1006.85 GB
Used                   : 2.74 GB
Free                   : 952.90 GB

NETWORK I/O
------------------------------------------------------------
Total Bytes Sent       : 390,949,245
Total Bytes Received   : 630,912,417
Upload Speed           : 712 B/s
Download Speed         : 836 B/s
============================================================

```
Requirements

Linux environment (tested on Ubuntu via WSL)

Python 3.8 or later

psutil Python library


Installation

  Clone the repository:
  
    git clone https://github.com/Arnav-techy/linux-resource-monitor.git
    cd linux-resource-monitor
    
  Create and activate a virtual environment (recommended):
  
    python3 -m venv venv
    source venv/bin/activate
  Install the required dependency:
  
    pip install psutil


How to Run

Run the program using:

  python Monitor_logic.py

The terminal screen refreshes automatically every 20 seconds

Press Ctrl + C to stop the monitor safe


How It Works (Briefly)

1. psutil is used to fetch system-level metrics such as CPU, memory, disk, and network data

2. Network speed is calculated by comparing byte counts between two timestamps

3. The terminal screen is cleared on every refresh to keep output clean

4. The program runs continuously until interrupted by the user

Why This Project

1. This project was created to:

2. Learn Linux system monitoring concepts

3. Understand CPU, memory, disk, and network metrics

4. Practice Python scripting in a Linux environment

5. Get hands-on experience with psutil, Git, and WSL

6. The focus of this project is correctness, clarity, and fundamentals rather than advanced UI features.

Possible Improvements

1. Add colored output or warning thresholds

2. Display top running processes

3. Add logging support

4. Convert the output into a full-scre


Author

Arnav Mishra


License

This project is intended for learning and personal use.


    
