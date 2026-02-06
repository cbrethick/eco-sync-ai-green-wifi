import psutil
import time
from datetime import datetime

_prev_bytes = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
_prev_time = time.time()

def collect():
    global _prev_bytes, _prev_time

    now = time.time()
    net = psutil.net_io_counters()
    current_bytes = net.bytes_sent + net.bytes_recv

    # Calculate traffic rate (MB per second)
    byte_diff = current_bytes - _prev_bytes
    time_diff = now - _prev_time

    traffic_rate = (byte_diff / (1024 * 1024)) / time_diff if time_diff > 0 else 0

    _prev_bytes = current_bytes
    _prev_time = now

    return {
        "time": datetime.now().strftime("%H:%M:%S"),
        "traffic_mb_s": round(traffic_rate, 4)
    }
