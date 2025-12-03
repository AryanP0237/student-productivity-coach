import tkinter as tk
import time
import threading

def start_timer(label, minutes):
    total = minutes * 60

    def countdown():
        for remaining in range(total, 0, -1):
            mins = remaining // 60
            secs = remaining % 60
            label.config(text=f"{mins:02d}:{secs:02d}")
            time.sleep(1)
        label.config(text="Done!")

    t = threading.Thread(target=countdown)
    t.start()