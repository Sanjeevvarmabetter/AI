import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def available_moves(board):
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]

def minmax(board, depth, is_maximizing):
    scores = {
        "X": 1,
        "O": -1,
        "draw": 0,
    }

    if check_winner(board, "X"):
        return scores["X"]
    if check_winner(board, "O"):
        return scores["O"]
    if is_draw(board):
        return scores["draw"]

    player = "X" if is_maximizing else "O"
    best_score = float("-inf") if is_maximizing else float("inf")

    for row, col in available_moves(board):
        board[row][col] = player
        score = minmax(board, depth + 1, not is_maximizing)
        board[row][col] = " "

        if is_maximizing:
            best_score = max(best_score, score)
        else:
            best_score = min(best_score, score)

    return best_score

def best_move(board):
    best_score = float("-inf")
    move = None

    for row, col in available_moves(board):
        board[row][col] = "X"
        score = minmax(board, 0, False)
        board[row][col] = " "

        if score > best_score:
            best_score = score
            move = (row, col)

    return move

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        player_row, player_col = map(int, input("Enter your move (row and column): ").split())
        if board[player_row][player_col] == " ":
            board[player_row][player_col] = "O"
        else:
            print("Invalid move. Try again.")
            continue

        if check_winner(board, "O"):
            print("You win!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        computer_row, computer_col = best_move(board)
        print(f"Computer's move: {computer_row}, {computer_col}")
        board[computer_row][computer_col] = "X"

        if check_winner(board, "X"):
            print("Computer wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        print_board(board)

if __name__ == "__main__":
    main()
