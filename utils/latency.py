import time

last_tick_time = None

def measure_latency(orderbook_data):
    """
    Measures internal latency between ticks (difference in timestamp).
    
    Parameters:
        orderbook_data (dict): Incoming orderbook tick with timestamp.
    
    Returns:
        float: Latency in milliseconds.
    """
    global last_tick_time
    timestamp_str = orderbook_data.get("timestamp")
    
    if not timestamp_str:
        return 0.0
    
    # Convert ISO timestamp to seconds
    tick_time = time.strptime(timestamp_str, "%Y-%m-%dT%H:%M:%SZ")
    tick_seconds = time.mktime(tick_time)

    if last_tick_time is None:
        last_tick_time = tick_seconds
        return 0.0
    
    latency = (tick_seconds - last_tick_time) * 1000  # ms
    last_tick_time = tick_seconds

    return round(latency, 2)
