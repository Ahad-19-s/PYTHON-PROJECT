import tkinter as tk
from tkinter import messagebox

# Quiz data
quiz = [
    {
        "question": "Who developed Python programming language?",
        "options": ["Dennis Ritchie", "Bjarne Stroustrup", "Guido van Rossum", "James Gosling"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "What year was Python first released?",
        "options": ["1989", "1991", "2000", "1995"],
        "answer": "1991"
    },
    {
        "question": "Which of the following is used to define a block of code in Python?",
        "options": ["Curly braces {}", "Parentheses ()", "Indentation", "Quotation marks"],
        "answer": "Indentation"
    },
    {
        "question": "Which keyword is used for function in Python?",
        "options": ["fun", "define", "def", "function"],
        "answer": "def"
    },
    {
        "question": "Which data type is immutable in Python?",
        "options": ["List", "Dictionary", "Set", "Tuple"],
        "answer": "Tuple"
    }
]

# Main app window
root = tk.Tk()
root.title("🧠 Python Quiz App")
root.geometry("600x400")
root.config(bg="#5619D0")

# Global variables
current_q = 0
score = 0

# Widgets
question_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="#f0f4f7", wraplength=500)
question_label.pack(pady=30)

var = tk.StringVar()

option_buttons = []
for i in range(4):
    btn = tk.Radiobutton(root, text="", variable=var, value="", font=("Arial", 14),
                         bg="#f0f4f7", anchor="w", padx=20)
    btn.pack(fill="x", padx=50, pady=5)
    option_buttons.append(btn)

# Functions
def load_question():
    global current_q
    q = quiz[current_q]
    question_label.config(text=f"Q{current_q + 1}: {q['question']}")
    var.set(None)
    for i, opt in enumerate(q["options"]):
        option_buttons[i].config(text=opt, value=opt)

def next_question():
    global current_q, score
    selected = var.get()
    if not selected:
        messagebox.showwarning("⚠️ Warning", "Please select an answer!")
        return
    if selected == quiz[current_q]["answer"]:
        score += 1
        messagebox.showinfo("✅ Correct!", "That's the right answer!")
    else:
        messagebox.showerror("❌ Wrong!", f"The correct answer was: {quiz[current_q]['answer']}")
    current_q += 1
    if current_q < len(quiz):
        load_question()
    else:
        show_result()

def show_result():
    messagebox.showinfo("🎯 Quiz Finished!", f"Your final score: {score}/{len(quiz)}")
    root.destroy()

# Next button
next_btn = tk.Button(root, text="Next ➡️", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white",
                     padx=20, pady=5, command=next_question)
next_btn.pack(pady=30)

# Start first question
load_question()

root.mainloop()
