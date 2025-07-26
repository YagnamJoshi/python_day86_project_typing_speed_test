import tkinter as tk
from book import Book
import time

# Global variable to store start time
start_time = None

def calculate_words_per_minute(reference_text, user_text, start, end):
    time_taken = (end - start) / 60  # time in minutes
    if time_taken == 0:
        return 0
    words = len(user_text.strip().split())
    return int(words / time_taken)

def start_typing():
    global start_time
    b = Book()
    theme, paragraph = b.generate()
    theme_text.config(text=f"Theme: {theme}")
    paragraph_box.config(state="normal")
    paragraph_box.delete("1.0", tk.END)
    paragraph_box.insert(tk.END, paragraph)
    paragraph_box.config(state="disabled")

    user_input_box.delete("1.0", tk.END)
    start_time = time.time()

def end_typing():
    global start_time
    end_time = time.time()

    paragraph = paragraph_box.get("1.0", tk.END).strip()
    user_input = user_input_box.get("1.0", tk.END).strip()

    if start_time is None:
        result_label.config(text="Press Start first!")
        return

    wpm = calculate_words_per_minute(paragraph, user_input, start_time, end_time)
    result_label.config(text=f"Your speed: {wpm} WPM")

# Tkinter GUI setup
app = tk.Tk()
app.geometry("700x650")
app.configure(bg="#d0eaff")
app.title("Typing Speed Test")

# Title
title = tk.Label(app, text="Typing Speed Test", font=("Arial", 28, "bold"), fg="#004080", bg="#d0eaff")
title.grid(row=0, column=0, columnspan=3, pady=(20, 10))

# Start Button
start_button = tk.Button(app, text="Start", font=("Arial", 14), fg="white", bg="#3399ff", width=10, command=start_typing)
start_button.grid(row=1, column=0, padx=20, pady=10)

# End Button
end_button = tk.Button(app, text="End", font=("Arial", 14), fg="white", bg="#ff6666", width=10, command=end_typing)
end_button.grid(row=1, column=2, padx=20, pady=10)

# Theme Text
theme_text = tk.Label(app, text="", font=("Arial", 16, "italic"), fg="#006699", bg="#d0eaff")
theme_text.grid(row=2, column=0, columnspan=3, pady=(10, 5))

# Paragraph Display (read-only)
paragraph_box = tk.Text(app, height=7, width=70, wrap="word", font=("Arial", 13), bg="white", fg="black")
paragraph_box.grid(row=3, column=0, columnspan=3, padx=20, pady=10)
paragraph_box.config(state="disabled")

# User Input Box
user_input_box = tk.Text(app, height=7, width=70, wrap="word", font=("Arial", 13), bg="white", fg="black")
user_input_box.grid(row=4, column=0, columnspan=3, padx=20, pady=10)

# Result Label
result_label = tk.Label(app, text="", font=("Arial", 14), fg="#004080", bg="#d0eaff")
result_label.grid(row=5, column=0, columnspan=3, pady=(10, 20))

app.mainloop()
