def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_draw(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, is_maximizing):
    if is_winner(board, 'X'):
        return -1
    if is_winner(board, 'O'):
        return 1
    if is_draw(board):
        return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            score = minimax(board, depth + 1, False)
            board[i][j] = ' '
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            score = minimax(board, depth + 1, True)
            board[i][j] = ' '
            best_score = min(best_score, score)
        return best_score

def best_move(board):
    best_score = -float('inf')
    move = None
    for i, j in get_empty_cells(board):
        board[i][j] = 'O'
        score = minimax(board, 0, False)
        board[i][j] = ' '
        if score > best_score:
            best_score = score
            move = (i, j)
    return move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    
    while not is_winner(board, 'X') and not is_winner(board, 'O') and not is_draw(board):
        print_board(board)
        
        player_i, player_j = map(int, input("Enter your move (row column): ").split())
        if board[player_i][player_j] == ' ':
            board[player_i][player_j] = 'X'
        else:
            print("Cell already taken. Try again.")
            continue
        
        if is_winner(board, 'X'):
            print_board(board)
            print("You win!")
            break
        elif is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        ai_i, ai_j = best_move(board)
        board[ai_i][ai_j] = 'O'
        
        if is_winner(board, 'O'):
            print_board(board)
            print("AI wins!")
            break
    
    print("Game over.")

if __name__ == "__main__":
    main()