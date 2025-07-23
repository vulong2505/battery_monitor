''' Checks threshold and triggers notifications '''

from plyer import notification
import config
import time

last_alert_time = {"low": 0, "high": 0}
SNOOZE_DURATION = 10 * 60  # 10 minutes

def check_alerts(status):
    ''' Sends a pop-up notification when threshold event triggers '''

    now = time.time()

    # Check to plug in
    if status["percent"] <= config.LOWER_BOUND_THRESHOLD and not status["plugged"]:
        if now - last_alert_time["low"] > SNOOZE_DURATION:
            notification.notify(title="Battery Low", message="Plug in charger!", timeout=5)
            last_alert_time["low"] = now
    
    # Check to unplug
    elif status["percent"] >= config.UPPER_BOUND_THRESHOLD and status["plugged"]:
        if now - last_alert_time["high"] > SNOOZE_DURATION:
            notification.notify(title="Battery High", message="Unplug your charger!", timeout=5)
            last_alert_time["high"] = now