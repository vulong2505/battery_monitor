''' Gather raw battery data with psutil.  '''

import psutil

def get_battery_status() -> dict:
    battery = psutil.sensors_battery()
    return {
        "percent": battery.percent,
        "plugged": battery.power_plugged,
        "secs_left": battery.secsleft
    }