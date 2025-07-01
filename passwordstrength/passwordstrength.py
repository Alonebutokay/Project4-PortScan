import tkinter as tk
import re
from tkinter import messagebox

try:
    import nltk
    from nltk.corpus import words
    nltk.download('words', quiet=True)
    nltk_words = set(words.words())
except ImportError:
    nltk_words = set()

def check_password_strength(password):
    suggestions = []
    strength = 0

    # Check length
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Use at least 12 characters.")

    # Check for lowercase
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        suggestions.append("Add lowercase letters.")

    # Check for uppercase
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        suggestions.append("Add uppercase letters.")

    # Check for numbers
    if re.search(r"\d", password):
        strength += 1
    else:
        suggestions.append("Add numbers.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        suggestions.append("Add special characters.")

    # Check for dictionary word
    if nltk_words:
        if password.lower() in nltk_words:
            suggestions.append("Avoid common dictionary words.")

    if strength >= 6:
        return "Strong", suggestions
    elif strength >= 4:
        return "Moderate", suggestions
    else:
        return "Weak", suggestions

def on_check():
    pwd = entry.get()
    if not pwd:
        messagebox.showwarning("Warning", "Please enter a password.")
        return

    result, tips = check_password_strength(pwd)
    result_label.config(text=f"Strength: {result}", fg="green" if result == "Strong" else "orange" if result == "Moderate" else "red")

    suggestions_box.delete(0, tk.END)
    for tip in tips:
        suggestions_box.insert(tk.END, tip)

# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack()

tk.Button(root, text="Check Strength", command=on_check).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

tk.Label(root, text="Suggestions:", font=("Arial", 12)).pack(pady=(10, 0))
suggestions_box = tk.Listbox(root, width=50, height=6)
suggestions_box.pack()

root.mainloop()

