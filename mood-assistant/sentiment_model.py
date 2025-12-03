#sentiment_model.py
from textblob import TextBlob
from datetime import datetime
import tkinter as tk

def classify(score):
    if score > 0.2:
        return "positive"
    elif score < -0.2:
        return "negative"
    else:
        return "neutral"

def motivate(mood):
    if mood == "positive":
        return "🔥 Keep going! Your momentum is your weapon."
    elif mood == "negative":
        return "💪 You got hit, but you're not done. One small step now."
    else:
        return "😐 Balanced. Not bad. Not great. But you can steer the wheel."

while True:
    text = input("\nEnter text (or 'q' to quit): ")
    if text.lower() == "q":
        print("thank you for using our program")
        break

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    mood = classify(polarity)

    print("Sentiment polarity:", polarity)
    print("Mood:", mood)
    print("Message:", motivate(mood))

    # Write to log file
    with open("mood_log.txt", "a") as f:
        f.write(f"{datetime.now()} — {mood} — {text}\n")

print("Exited program.")