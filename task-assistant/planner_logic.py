def generate_plan(task, mood):
    task = task.strip()

    if not task:
        return "No task entered."

    base = f"Task: {task}\n\nRecommended Steps:\n"

    if mood == "positive":
        steps = [
            "1. Break the task into 3 mini-parts.",
            "2. Start with the hardest part first.",
            "3. Do a 25-minute deep focus sprint.",
            "4. Take a 5-minute break.",
            "5. Finish the remaining parts in one more sprint."
        ]
    elif mood == "negative":
        steps = [
            "1. Start with the easiest possible version.",
            "2. Do just 10 minutes — no more.",
            "3. Once started, momentum will build.",
            "4. Reward yourself with a break after.",
            "5. If energy returns, do a 25-minute sprint."
        ]
    else:
        steps = [
            "1. Break into 2 medium parts.",
            "2. Do a 20-minute focused block.",
            "3. Take a 5-minute break.",
            "4. Finish the second part calmly."
        ]

    return base + "\n".join(steps)