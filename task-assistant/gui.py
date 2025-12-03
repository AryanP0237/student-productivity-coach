import tkinter as tk
from planner_logic import generate_plan
from timer import start_timer
import datetime
from tkinter import messagebox

root = tk.Tk()
last_session = None
root.title("Task Coach")

task_label = tk.Label(root, text="Enter task:")
task_label.pack()

task_entry = tk.Text(root, height=3, width=40)
task_entry.pack()

mood_label = tk.Label(root, text="Select mood:")
mood_label.pack()

mood_var = tk.StringVar(root)
mood_var.set("neutral")

mood_menu = tk.OptionMenu(root, mood_var, "positive", "neutral", "negative")
mood_menu.pack()

def make_plan():
    task = task_entry.get("1.0", tk.END)
    mood = mood_var.get()
    plan = generate_plan(task, mood)
    global last_session
    last_session = {
        "timestamp": datetime.datetime.now(),
        "task": task.strip(),
        "mood": mood,
        "plan": plan
    }
    result_label.config(text=plan)

def save_session():
    global last_session
    if not last_session:
        messagebox.showinfo("Nothing to save", "Generate a plan first before saving.")
        return

    try:
        # Format timestamp for human-readable log
        ts_str = last_session["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
        log_entry = (
            f"\n-----\n"
            f"Time: {ts_str}\n"
            f"Mood: {last_session['mood']}\n"
            f"Task: {last_session['task']}\n"
            f"Plan:\n{last_session['plan']}\n"
        )

        with open("session_log.txt", "a", encoding="utf-8") as f:
            f.write(log_entry)

        messagebox.showinfo("Saved", "Session saved to session_log.txt")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save session: {e}")

plan_button = tk.Button(root, text="Generate Plan", command=make_plan)
plan_button.pack()

save_button = tk.Button(root, text="Save Session", command=save_session)
save_button.pack()

result_label = tk.Label(root, text="", justify="left")
result_label.pack()

timer_label = tk.Label(root, text="Timer will appear here")
timer_label.pack()

minutes_label = tk.Label(root, text="Focus minutes:")
minutes_label.pack()

minutes_entry = tk.Entry(root)
minutes_entry.insert(0, "25")  # default value
minutes_entry.pack()

def start_custom_timer():
    minutes_str = minutes_entry.get().strip()
    if not minutes_str:
        messagebox.showinfo("No duration", "Please enter focus minutes.")
        return
    try:
        minutes = int(minutes_str)
        if minutes <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a positive whole number of minutes.")
        return

    start_timer(timer_label, minutes)

start_timer_button = tk.Button(root, text="Start Timer", command=start_custom_timer)
start_timer_button.pack()

root.mainloop()