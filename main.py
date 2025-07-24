from core.monitor import get_battery_status
from core.logger import log_status
from core.notifier import check_alerts
from core.battery_state import update_state, get_logging_data
from core.utils import set_writing_flag, setup_signal_handler
import time
import config

def main():
    setup_signal_handler()

    print('''
   ___       __  __                 __  ___          _ __
  / _ )___ _/ /_/ /____ ______ __  /  |/  /__  ___  (_) /____  ____
 / _  / _ `/ __/ __/ -_) __/ // / / /|_/ / _ \/ _ \/ / __/ _ \/ __/
/____/\_,_/\__/\__/\__/_/  \_, / /_/  /_/\___/_//_/_/\__/\___/_/
                          /___/
''')
    print("Starting Battery Monitor...")

    while True:
        status = get_battery_status()
        update_state(status)
        logging_data = get_logging_data(status)

        set_writing_flag(True)
        log_status(logging_data)
        set_writing_flag(False)

        check_alerts(status)
        time.sleep(config.LOG_INTERVAL)

if __name__ == "__main__":
    main()