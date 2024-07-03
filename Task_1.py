#TIC TAC TOE GAME

import math

print("-----------------------------------")
print("*********TIC TAC TOE GAME**********")
print("-----------------------------------")

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if check_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("********Welcome*******")
    print_board(board)

    while True:
        # User move
        while True:
            try:
                move = int(input("Enter your move (1-9): ")) - 1
                if board[move // 3][move % 3] == ' ':
                    board[move // 3][move % 3] = 'X'
                    break
                else:
                    print("Invalid move! Cell already taken.")
            except (ValueError, IndexError):
                print("Invalid move! Enter a number between 1 and 9.")

        print_board(board)

        if check_winner(board, 'X'):
            print("Congratulations! You win!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

        # Computer move
        move = best_move(board)
        if move:
            board[move[0]][move[1]] = 'O'
            print("Computer move:")
            print_board(board)

            if check_winner(board, 'O'):
                print("Computer wins! Better luck next time.")
                break
            if check_draw(board):
                print("It's a draw!")
                break

if __name__ == "__main__":
    play_game()
