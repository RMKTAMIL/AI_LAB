"""Tic-Tac-Toe agent using Minimax with Alpha-Beta Pruning (You = O, AI = X)"""
WINS = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def winner(b):
    for x, y, z in WINS:
        if b[x] != ' ' and b[x] == b[y] == b[z]:
            return b[x]
    return 'D' if ' ' not in b else None

def minimax(b, d, alpha, beta, maxi):
    r = winner(b)
    if r:
        return {'X': 10 - d, 'O': d - 10, 'D': 0}[r]   # +10 AI win, -10 human win, 0 draw
    best = -99 if maxi else 99
    for i in range(9):
        if b[i] == ' ':
            b[i] = 'X' if maxi else 'O'
            s = minimax(b, d + 1, alpha, beta, not maxi)
            b[i] = ' '
            if maxi:
                best = max(best, s); alpha = max(alpha, best)
            else:
                best = min(best, s); beta = min(beta, best)
            if beta <= alpha:                            # alpha-beta cut-off
                break
    return best

def ai_move(b):
    def score(i):
        b[i] = 'X'; s = minimax(b, 1, -99, 99, False); b[i] = ' '
        return s
    return max((i for i in range(9) if b[i] == ' '), key=score)

def show(b):
    for i in range(0, 9, 3):
        print(' | '.join(c if c != ' ' else str(i + j) for j, c in enumerate(b[i:i+3])))
    print()

b = [' '] * 9
while not winner(b):
    show(b)
    m = int(input("Your move (0-8): "))
    if not 0 <= m < 9 or b[m] != ' ':
        print("Invalid move!"); continue
    b[m] = 'O'
    if not winner(b):
        b[ai_move(b)] = 'X'
show(b)
print({'X': 'AI wins!', 'O': 'You win!', 'D': "It's a draw!"}[winner(b)])
