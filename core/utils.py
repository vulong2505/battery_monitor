''' Helper utility functions for battery monitoring '''

import signal
import sys
import time

# Global flag to track if we're currently writing to CSV
_writing_to_csv = False

def set_writing_flag(writing):
    ''' Set the global flag indicating if we're currently writing to CSV '''

    global _writing_to_csv
    _writing_to_csv = writing

def setup_signal_handler():
    ''' Setup signal handlers for graceful shutdown on Ctrl+C or system kill '''

    def signal_handler(sig, frame):
        ''' Handle termination signals gracefully '''

        print(f"\n🔋 Battery Monitor shutting down...")
        
        # Wait for any ongoing CSV write to complete
        if _writing_to_csv:
            print("⏳ Waiting for log write to complete...")
            while _writing_to_csv:
                time.sleep(0.1)
        
        print("✅ Cleanup complete. Goodbye!")
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)   # Ctrl+C
    signal.signal(signal.SIGTERM, signal_handler)  # System shutdown/kill command

# TODO: Plug this in with Tkinter custom notification
def format_seconds(seconds):
    ''' Display time remaining in a human-readable format, e.g. 1h 32m instead of 5523 seconds. '''

    mins, secs = divmod(seconds, 60)
    hrs, mins = divmod(mins, 60)
    return f"{hrs}h {mins}m" if hrs else f"{mins}m"
