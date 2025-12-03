def save_plan():
    task = task_entry.get("1.0", tk.END).strip()
    mood = mood_var.get()
    plan = result_label.cget("text")

    if not task or not plan:
        return

    with open("task_log.txt", "a") as file:
        file.write("\n---\n")
        file.write(f"Mood: {mood}\n")
        file.write(f"Task: {task}\n")
        file.write(f"Plan:\n{plan}\n")

save_button = tk.Button(root, text="Save Plan", command=save_plan)
save_button.pack()