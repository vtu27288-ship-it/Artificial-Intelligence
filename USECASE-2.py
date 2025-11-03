# Game Playing Agent - Tic Tac Toe using Minimax Algorithm

import math

# Initialize board
board = [' ' for _ in range(9)]

def print_board(board):
    for i in range(3):
        print(board[3*i], '|', board[3*i+1], '|', board[3*i+2])
        if i < 2:
            print("---------")

def check_winner(board, player):
    win_cond = [(0,1,2),(3,4,5),(6,7,8),
                (0,3,6),(1,4,7),(2,5,8),
                (0,4,8),(2,4,6)]
    for (x, y, z) in win_cond:
        if board[x] == board[y] == board[z] == player:
            return True
    return False

def minimax(board, depth, isMaximizing):
    if check_winner(board, 'X'):
        return 1
    elif check_winner(board, 'O'):
        return -1
    elif ' ' not in board:
        return 0

    if isMaximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

# Main game loop
print("Welcome to Tic Tac Toe!")
print_board(board)

while True:
    # Human move
    player_move = int(input("Enter your move (1-9): ")) - 1
    if board[player_move] == ' ':
        board[player_move] = 'O'
    else:
        print("Invalid move, try again.")
        continue

    if check_winner(board, 'O'):
        print_board(board)
        print("You Win!")
        break

    if ' ' not in board:
        print_board(board)
        print("It's a Draw!")
        break

    # Computer move
    comp_move = best_move(board)
    board[comp_move] = 'X'

    print_board(board)

    if check_winner(board, 'X'):
        print("Computer Wins!")
        break

    if ' ' not in board:
        print("It's a Draw!")
        break
