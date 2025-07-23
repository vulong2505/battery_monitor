''' 
Extended data tracking for our current battery state. Works in tandem with raw data captured from monitor.py.
This script adds processing logic for extended data analytics to create a rich snapshot of our battery state.

TODO: Get more analytics with on temperature, power draw from SSD, RAM, etc.
'''

import time
import psutil
from datetime import datetime

battery_state = {
    "last_plugged": None,
    "last_unplugged": None,
    "time_at_100_start": None,
    "accumulated_100_secs": 0,
    "last_percent": None,
    "was_plugged": None     # None = not yet initialized, prevents false transitions
}

def update_state(status):
    ''' Extended data tracking for our current battery state. '''

    now = time.time()

    # Transition: Unplugged → Plugged
    if status["plugged"] and battery_state["was_plugged"] == False:
        battery_state["last_plugged"] = now

    # Transition: Plugged → Unplugged
    elif not status["plugged"] and battery_state["was_plugged"] == True:
        battery_state["last_unplugged"] = now

    # Track time at 100%
    if status["percent"] == 100 and status["plugged"]:
        if battery_state["time_at_100_start"] is None:
            battery_state["time_at_100_start"] = now
        else:
            battery_state["accumulated_100_secs"] = int(now - battery_state["time_at_100_start"])
    else:
        battery_state["time_at_100_start"] = None

    # Update flag
    battery_state["was_plugged"] = status["plugged"]

def get_logging_data(status) -> dict:
    """Prepare all data needed for logging, including enriched battery state."""

    now = time.time()

    # Process secs_left for better logging
    secs_left = status['secs_left']
    if secs_left == psutil.POWER_TIME_UNLIMITED:
        secs_left = "UNLIMITED"     # When plugged in, no time limit
    elif secs_left == psutil.POWER_TIME_UNKNOWN:
        secs_left = "UNKNOWN"       # System can't calculate remaining time

    # Process last_plugged and last_unplugged events for better logging
    if battery_state["last_plugged"]:
        since_plug = int(now - battery_state["last_plugged"])
    else:
        since_plug = "NO_PLUG_EVENT"  # Never been plugged since monitoring started
    
    if battery_state["last_unplugged"]:
        since_unplug = int(now - battery_state["last_unplugged"])
    else:
        since_unplug = "NO_UNPLUG_EVENT"  # Never been unplugged since monitoring started

    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "epoch_time": int(now),
        "percent": status["percent"],
        "plugged": status["plugged"],
        "secs_left": secs_left,
        "time_at_100": battery_state["accumulated_100_secs"],
        "since_last_plug": since_plug,
        "since_last_unplug": since_unplug
    }

