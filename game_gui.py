import numpy as np
import tkinter as tk
from tkinter import messagebox

rows = 3
columns = 3

def mark(row, col, player):
    board[row][col] = player

def is_valid_mark(row, col):
    return board[row][col] == 0

def is_board_full():
    for i in range(rows):
        for j in range(columns):
            if board[i][j] == 0:
                return False
    return True

def is_winning_mark(player):
    for i in range(rows):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    for j in range(columns):
        if board[0][j] == player and board[1][j] == player and board[2][j] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True
    return False

def on_click(row, col):
    global turn, gameover

    if not gameover and is_valid_mark(row, col):
        if turn % 2 == 0:
            mark(row, col, 1)
            if is_winning_mark(1):
                messagebox.showinfo("Game Over", "Player 1 (X) won!") #tkinter lib -> messagebox
                game_over()
        else:
            mark(row, col, 2)
            if is_winning_mark(2):
                messagebox.showinfo("Game Over", "Player 2 (O) won!")
                game_over()

        if is_board_full() and not is_winning_mark(1) and not is_winning_mark(2):
            messagebox.showinfo("Game Over", "It's a Draw!")
            game_over()

        turn += 1
        update_board()

def update_board():
    for i in range(rows):
        for j in range(columns):
            cell_value = board[i][j]
            cell_text = "X" if cell_value == 1 else "O" if cell_value == 2 else ""
            buttons[i][j].config(text=cell_text)

def game_over():
    global gameover
    gameover = True

# Create the GUI
root = tk.Tk()
root.title("Tic-Tac-Toe")

board = np.zeros((rows, columns))
buttons = [[None for _ in range(columns)] for _ in range(rows)]

for i in range(rows):
    for j in range(columns):
        buttons[i][j] = tk.Button(root, text="", font=("Helvetica", 20), width=6, height=4,
                                  command=lambda row=i, col=j: on_click(row, col))
        buttons[i][j].grid(row=i, column=j)

turn = 0
gameover = False

root.mainloop()
