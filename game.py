
import numpy as np



rows = 3
coloum = 3

def mark(row,col,player):
    board[row][col] = player

def is_valid_mark(row,col):
    return board[row][col] == 0

def is_board_full():
    for i in range(coloum):
        for j in range(rows):
            if board[i][j] == 0:
                return False
        return True
    

board = np.zeros((rows,coloum))

gameover = False
turn = 0
while not gameover:
    if turn % 2 == 0:
        row = int(input("Player one : "))
        col = int(input("player one : "))
        if is_valid_mark(row,col):
            mark(row,col,1)

        else:
            turn-=1
    else:
        row = int(input("Player 2 :" ))
        col = int(input("Player 2 : "))

        if is_valid_mark(row,col):
            mark(row,col,2)
        else:
            turn -= 1
        
    turn += 1
    print(board)
