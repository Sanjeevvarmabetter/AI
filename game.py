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
    
def is_wining_mark(player):
    if player == 1:
        a = "Player 1 won"
    else:
        a = "Player 2 won"
    for i in range(rows):
        if board[i][0] == player and board[i][1] == player[i][2] == player:
            print(a)
            return True
    for j in range(coloum):
        if board[0][j] == player and board[1][j] == player and board[2][j] == player:
            print(a)
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        print(a)
        return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        print(a)
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
