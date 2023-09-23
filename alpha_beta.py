import math

# Constants for the Tic Tac Toe game
WIN = 10
DRAW = 0
LOSS = -10
AI_MARKER = 'O'
PLAYER_MARKER = 'X'
EMPTY_SPACE = '-'
INF = float('inf')

# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

# Function to check if the game is over
def is_game_over(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY_SPACE:
            return True
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY_SPACE:
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY_SPACE:
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY_SPACE:
        return True
    if any(EMPTY_SPACE in row for row in board):
        return False
    return True

# Function to evaluate the score of the board
def evaluate(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == AI_MARKER:
                return WIN
            elif board[i][0] == PLAYER_MARKER:
                return LOSS

        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == AI_MARKER:
                return WIN
            elif board[0][i] == PLAYER_MARKER:
                return LOSS

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == AI_MARKER:
            return WIN
        elif board[0][0] == PLAYER_MARKER:
            return LOSS

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == AI_MARKER:
            return WIN
        elif board[0][2] == PLAYER_MARKER:
            return LOSS

    return DRAW

# Function to perform minimax with alpha-beta pruning
def minimax(board, depth, alpha, beta, is_maximizing):
    score = evaluate(board)

    if score == WIN:
        return score - depth

    if score == LOSS:
        return score + depth

    if is_game_over(board):
        return DRAW

    if is_maximizing:
        max_eval = -INF
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY_SPACE:
                    board[i][j] = AI_MARKER
                    eval = minimax(board, depth + 1, alpha, beta, False)
                    board[i][j] = EMPTY_SPACE
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = INF
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY_SPACE:
                    board[i][j] = PLAYER_MARKER
                    eval = minimax(board, depth + 1, alpha, beta, True)
                    board[i][j] = EMPTY_SPACE
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to find the best move for the AI using minimax and alpha-beta pruning
def find_best_move(board):
    best_move = None
    best_val = -INF
    alpha = -INF
    beta = INF

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY_SPACE:
                board[i][j] = AI_MARKER
                move_val = minimax(board, 0, alpha, beta, False)
                board[i][j] = EMPTY_SPACE

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Main function to play the Tic Tac Toe game
def play_game():
    board = [[EMPTY_SPACE for _ in range(3)] for _ in range(3)]
    print("Tic Tac Toe Game")
    print_board(board)

    while not is_game_over(board):
        print("Player's turn (row, col):")
        player_row, player_col = map(int, input().split())
        if board[player_row][player_col] != EMPTY_SPACE:
            print("Cell already taken. Try again.")
            continue

        board[player_row][player_col] = PLAYER_MARKER
        print_board(board)

        if is_game_over(board):
            break

        print("AI's turn:")
        ai_row, ai_col = find_best_move(board)
        board[ai_row][ai_col] = AI_MARKER
        print_board(board)

    score = evaluate(board)
    if score == WIN:
        print("AI wins!")
    elif score == LOSS:
        print("Player wins!")
    else:
        print("It's a draw!")

# Run the game
if __name__ == "__main__":
    play_game()
