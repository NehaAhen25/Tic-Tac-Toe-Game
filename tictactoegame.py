import tkinter as tk
from tkinter import messagebox
import winsound

def check_winner():
    global winner
    for combo in [[0,1,2],[3,4,5],[6,7,8],
                  [0,3,6],[1,4,7],[2,5,8],
                  [0,4,8],[2,4,6]]:
        if buttons[combo[0]]['text'] == buttons[combo[1]]['text'] == buttons[combo[2]]['text'] != "":
            for i in combo:
                buttons[i].config(bg='green')
            # Play win sound (use WAV format here)
            winsound.PlaySound("C:\\game-win-sound.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)
            messagebox.showinfo("Tic-Tac-Toe", f"{buttons[combo[0]]['text']} wins!")
            winner = True
            return

    # Check for tie (draw)
    if all(btn['text'] != "" for btn in buttons) and not winner:
        winsound.MessageBeep(winsound.MB_ICONASTERISK)  # System beep for tie
        messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")

def button_click(index):
    global current_player
    if buttons[index]['text'] == "" and not winner:
        buttons[index]['text'] = current_player
        check_winner()
        if not winner:
            toggle_player()

def toggle_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"
    label.config(text=f"Player {current_player}'s Turn")

# Set up the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Initialize game variables
current_player = "X"
winner = False

# Create buttons
buttons = [tk.Button(root, text="", font=('normal', 25), width=6, height=2,
            command=lambda i=i: button_click(i)) for i in range(9)]

# Place buttons in grid
for i, btn in enumerate(buttons):
    btn.grid(row=i//3, column=i%3)

# Add player label
label = tk.Label(root, text=f"Player {current_player}'s Turn", font=('normal', 16))
label.grid(row=3, column=0, columnspan=3)

# Run the app
root.mainloop()




