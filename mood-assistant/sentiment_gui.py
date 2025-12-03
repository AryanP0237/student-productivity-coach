# sentiment_gui.py

import tkinter as tk
from textblob import TextBlob

def analyze_sentiment():
    """Read text from the box, run TextBlob, and show result."""
    text = input_box.get("1.0", tk.END).strip()
    if not text:
        result_var.set("Please type something first.")
        return

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity      # -1 (negative) to +1 (positive)
    subjectivity = blob.sentiment.subjectivity  # 0 (objective) to 1 (subjective)

    # Simple interpretation
    if polarity > 0.2:
        mood = "Positive 🙂"
    elif polarity < -0.2:
        mood = "Negative 🙁"
    else:
        mood = "Neutral 😐"

    result_var.set(
        f"Sentiment: {mood}\n"
        f"Polarity: {polarity:.3f}\n"
        f"Subjectivity: {subjectivity:.3f}"
    )

# ----- GUI SETUP -----

root = tk.Tk()
root.title("Sentiment Coach")
root.geometry("500x350")  # width x height

# Label
title_label = tk.Label(root, text="Type your text below:", font=("Helvetica", 12))
title_label.pack(pady=(10, 0))

# Multi-line text box
input_box = tk.Text(root, height=6, width=55)
input_box.pack(padx=10, pady=10)

# Analyze button
analyze_button = tk.Button(root, text="Analyze Sentiment", command=analyze_sentiment)
analyze_button.pack(pady=5)

# Result label
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Helvetica", 11), justify="left")
result_label.pack(padx=10, pady=10)

# Start the event loop
root.mainloop()