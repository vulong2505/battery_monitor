''' Logs battery status into a CSV at logs/ '''

import csv
import os
import time
from datetime import datetime
from core.battery_state import battery_state
import config

def log_status(status):
    if not os.path.exists("logs"):
        os.makedirs("logs")

    file_exists = os.path.isfile(config.LOG_FILE)

    with open(config.LOG_FILE, 'a', newline='') as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "timestamp", "epoch_time", "percent", "plugged", "secs_left",
                "time_at_100", "since_last_plug", "since_last_unplug"
            ])

        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        now_epoch = int(time.time())

        time_at_100 = battery_state["accumulated_100_secs"]
        since_plug = int(time.time() - battery_state["last_plugged"]) if battery_state["last_plugged"] else ""
        since_unplug = int(time.time() - battery_state["last_unplugged"]) if battery_state["last_unplugged"] else ""

        writer.writerow([
            now_str,
            now_epoch,
            status["percent"],
            status["plugged"],
            status["secs_left"],
            time_at_100,
            since_plug,
            since_unplug
        ])
