import math

# Initialize board
board = [' ' for _ in range(9)]

def print_board():
    print()
    for i in range(3):
        print(board[i*3], "|", board[i*3+1], "|", board[i*3+2])
        if i < 2:
            print("--+---+--")
    print()

def check_winner(player):
    win_combinations = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    return any(board[a]==board[b]==board[c]==player for a,b,c in win_combinations)

def is_draw():
    return ' ' not in board

def minimax(is_maximizing):
    if check_winner('O'):
        return 1
    if check_winner('X'):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'

def human_move():
    move = int(input("Enter position (0-8): "))
    if board[move] == ' ':
        board[move] = 'X'
    else:
        print("Invalid move!")
        human_move()

# Game Loop
print("Tic-Tac-Toe AI")
print("You are X, AI is O")
print("Positions are numbered from 0 to 8")

print_board()

while True:
    human_move()
    print_board()
    if check_winner('X'):
        print("🎉 You Win!")
        break
    if is_draw():
        print("🤝 Draw!")
        break

    ai_move()
    print("AI's Move:")
    print_board()
    if check_winner('O'):
        print("🤖 AI Wins!")
        break
