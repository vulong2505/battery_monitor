''' Helper utility functions for battery monitoring '''

# TODO: Plug this in with Tkinter custom notification
def format_seconds(seconds):
    ''' Display time remaining in a human-readable format, e.g. 1h 32m instead of 5523 seconds. '''

    mins, secs = divmod(seconds, 60)
    hrs, mins = divmod(mins, 60)
    return f"{hrs}h {mins}m" if hrs else f"{mins}m"