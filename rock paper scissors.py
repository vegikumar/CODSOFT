import tkinter as tk
from tkinter import messagebox
import random
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw"
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        return "You win!"
    else:
        return "You lose"
def handle_choice(user_choice):
    global user_score, computer_score
    user_choice -= 1
    computer_choice = random.randint(0, 2)
    result = determine_winner(user_choice, computer_choice)
    if "win" in result:
        user_score += 1
    elif "lose" in result:
        computer_score += 1
    update_scores()
    play_again()
def update_scores():
    user_score_label.config(text="Your Score: " + str(user_score))
    computer_score_label.config(text="Computer Score: " + str(computer_score))
def play_again():
    answer = messagebox.askyesno("Play Again", "Do you want to play again?")
    if answer:
        pass
    else:
        root.destroy()
user_score = 0
computer_score = 0
root = tk.Tk()
root.geometry("200x200")
root.title("Rock Paper Scissors")
rock_button = tk.Button(root, text="Rock", command=lambda: handle_choice(1))
rock_button.pack(pady=5)
paper_button = tk.Button(root, text="Paper", command=lambda: handle_choice(2))
paper_button.pack(pady=5)
scissors_button = tk.Button(root, text="Scissors", command=lambda: handle_choice(3))
scissors_button.pack(pady=5)
user_score_label = tk.Label(root, text="Your Score: " + str(user_score))
user_score_label.pack()
computer_score_label = tk.Label(root, text="Computer Score: " + str(computer_score))
computer_score_label.pack()
root.mainloop()
