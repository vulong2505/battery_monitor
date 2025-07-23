from core.monitor import get_battery_status
from core.logger import log_status
from core.notifier import check_alerts
from core.battery_state import update_state
import time
import config

while True:
    status = get_battery_status()
    update_state(status)
    log_status(status)
    check_alerts(status)
    time.sleep(config.LOG_INTERVAL)
