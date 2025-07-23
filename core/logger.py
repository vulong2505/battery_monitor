''' Logs battery status into a CSV at logs/ '''

import csv
import os
import config

def log_status(status):
    ''' Writer to CSV file '''
    
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

        writer.writerow([
            status["timestamp"],
            status["epoch_time"],
            status["percent"],
            status["plugged"],
            status["secs_left"],
            status["time_at_100"],
            status["since_last_plug"],
            status["since_last_unplug"]
        ])
