''' 
Extended data tracking for our current battery state. Works in tandem with raw data captured from monitor.py.
This script adds processing logic for extended data analytics to create a rich snapshot of our battery state.

TODO: Get more analytics with on temperature, power draw from SSD, RAM, etc.
'''

import time

battery_state = {
    "last_plugged": None,
    "last_unplugged": None,
    "time_at_100_start": None,
    "accumulated_100_secs": 0,
    "last_percent": None,
    "was_plugged": None
}

def update_state(current_status):
    now = time.time()

    # Transition: Unplugged → Plugged
    if current_status["plugged"] and battery_state["was_plugged"] == False:
        battery_state["last_plugged"] = now

    # Transition: Plugged → Unplugged
    elif not current_status["plugged"] and battery_state["was_plugged"] == True:
        battery_state["last_unplugged"] = now

    # Track time at 100%
    if current_status["percent"] == 100 and current_status["plugged"]:
        if battery_state["time_at_100_start"] is None:
            battery_state["time_at_100_start"] = now
        else:
            battery_state["accumulated_100_secs"] = int(now - battery_state["time_at_100_start"])
    else:
        battery_state["time_at_100_start"] = None

    # Update flag
    battery_state["was_plugged"] = current_status["plugged"]
