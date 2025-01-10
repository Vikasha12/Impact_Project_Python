import tkinter as tk
import random

# Function to handle game logic
def play_game(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    
    # Determine computer's choice
    comp_choice = random.choice(choices)
    
    # Determine the result
    if user_choice == comp_choice:
        result = "It's a draw!"
    elif (user_choice == 'Rock' and comp_choice == 'Scissors') or \
         (user_choice == 'Paper' and comp_choice == 'Rock') or \
         (user_choice == 'Scissors' and comp_choice == 'Paper'):
        result = "You win!"
    else:
        result = "Computer wins!"
    
    # Update the labels with the result
    comp_choice_label.config(text=f"Computer chose: {comp_choice}")
    result_label.config(text=result)

# Function to restart the game
def restart_game():
  comp_choice_label.config(text="Computer chose: ")
  result_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors Game")

# Set up the instructions label
instructions_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14))
instructions_label.pack(pady=10)

# Buttons for user choices
rock_button = tk.Button(root, text="Rock", width=20, height=2, command=lambda: play_game('Rock'))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=20, height=2, command=lambda: play_game('Paper'))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=20, height=2, command=lambda: play_game('Scissors'))
scissors_button.pack(pady=5)

# Label to show the computer's choice
comp_choice_label = tk.Label(root, text="Computer chose: ", font=("Arial", 12))
comp_choice_label.pack(pady=10)

# Label to show the result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Restart button to reset the game
restart_button = tk.Button(root, text="Restart Game", width=20, height=2, command=restart_game)
restart_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()