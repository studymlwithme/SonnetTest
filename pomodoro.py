import time

def pomodoro_timer(work_duration=25, short_break=5, long_break=15, cycles=4):
    """
    A simple Pomodoro Timer.
    
    :param work_duration: Duration of a work interval in minutes.
    :param short_break: Duration of a short break in minutes.
    :param long_break: Duration of a long break in minutes.
    :param cycles: Number of work cycles before a long break.
    """
    for cycle in range(1, cycles + 1):
        print(f"Pomodoro {cycle} of {cycles} started. Time to focus!")
        countdown(work_duration * 60, "Work interval")

        if cycle < cycles:
            print(f"Work interval complete! Take a short {short_break}-minute break.")
            countdown(short_break * 60, "Short break")
        else:
            print(f"You've completed {cycles} cycles! Take a long {long_break}-minute break.")
            countdown(long_break * 60, "Long break")
            print("All Pomodoro cycles finished!")
            

def countdown(seconds, label="Timer"):
    """
    Displays a countdown in mm:ss format.
    
    :param seconds: Number of seconds for countdown.
    :param label: Description or label for the countdown.
    """
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer_str = f"{mins:02d}:{secs:02d}"
        print(f"{label}: {timer_str}", end="\r")
        time.sleep(1)
        seconds -= 1
    print()  # Move to a new line after the countdown ends

if __name__ == "__main__":
    # You can customize these durations as you like.
    # The typical Pomodoro cycle is 25 minutes work, 5 minutes short break, and 15 minutes long break.
    pomodoro_timer(work_duration=25, short_break=5, long_break=15, cycles=4)

