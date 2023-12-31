import random

pieceScore = {"K": 20000, "Q": 900, "R": 500, "B": 330, "N": 320, "P": 100}
CHECKMATE = 30300
STALEMATE = 0
DEPTH = 2

# on a affecté un score à chaque position pour faire une difference entre les positions bonnes et mauvaises
# une position négative est mauvaise, positive est bonne et nulle est neutre
# score pour les pièces blanches
White_knight_Scores = [[-50, -40, -30, -30, -30, -30, -40, -50],
                       [-40, -20, 0, 0, 0, 0, -20, -40],
                       [-30, 0, 10, 15, 15, 10, 0, -30],
                       [-30, 5, 15, 20, 20, 15, 5, -30],
                       [-30, 0, 15, 20, 20, 15, 0, -30],
                       [-30, 5, 10, 15, 15, 10, 5, -30],
                       [-40, -20, 0, 5, 5, 0, -20, -40],
                       [-50, -40, -30, -30, -30, -30, -40, -50]
                       ]
White_Bishop_Scores = [[-20, -10, -10, -10, -10, -10, -10, -20],
                       [-10, 0, 0, 0, 0, 0, 0, -10],
                       [-10, 0, 5, 10, 10, 5, 0, -10],
                       [-10, 5, 5, 10, 10, 5, 5, -10],
                       [-10, 0, 10, 10, 10, 10, 0, -10],
                       [-10, 10, 10, 10, 10, 10, 10, -10],
                       [-10, 5, 0, 0, 0, 0, 5, -10],
                       [-20, -10, -10, -10, -10, -10, -10, -20]]
White_Queen_Scores = [
    [-20, -10, -10, -5, -5, -10, -10, -20],
    [-10, 0, 0, 0, 0, 0, 0, -10],
    [-10, 0, 5, 5, 5, 5, 0, -10],
    [-5, 0, 5, 5, 5, 5, 0, -5],
    [0, 0, 5, 5, 5, 5, 0, -5],
    [-10, 5, 5, 5, 5, 5, 0, -10],
    [-10, 0, 5, 0, 0, 0, 0, -10],
    [-20, -10, -10, -5, -5, -10, -10, -20]
]

White_Rook_Scores = [[0, 0, 0, 0, 0, 0, 0, 0],
                     [5, 10, 10, 10, 10, 10, 10, 5],
                     [-5, 0, 0, 0, 0, 0, 0, -5],
                     [-5, 0, 0, 0, 0, 0, 0, -5],
                     [-5, 0, 0, 0, 0, 0, 0, -5],
                     [-5, 0, 0, 0, 0, 0, 0, -5],
                     [-5, 0, 0, 0, 0, 0, 0, -5],
                     [0, 0, 0, 5, 5, 0, 0, 0]]

White_Pawn_Scores = [[0, 0, 0, 0, 0, 0, 0, 0],
                     [50, 50, 50, 50, 50, 50, 50, 50],
                     [10, 10, 20, 30, 30, 20, 10, 10],
                     [5, 5, 10, 25, 25, 10, 5, 5],
                     [0, 0, 0, 20, 20, 0, 0, 0],
                     [5, -5, -10, 0, 0, -10, -5, 5],
                     [5, 10, 10, -20, -20, 10, 10, 5],
                     [0, 0, 0, 0, 0, 0, 0, 0]]

eg_White_King_Scores = [[-30, -40, -40, -50, -50, -40, -40, -30],
                        [-30, -40, -40, -50, -50, -40, -40, -30],
                        [-30, -40, -40, -50, -50, -40, -40, -30],
                        [-30, -40, -40, -50, -50, -40, -40, -30],
                        [-20, -30, -30, -40, -40, -30, -30, -20],
                        [-10, -20, -20, -20, -20, -20, -20, -10],
                        [20, 20, 0, 0, 0, 0, 20, 20],
                        [20, 30, 10, 0, 0, 10, 30, 20]]

# *****************************************************************************************************************************************************************************
# score pour les pièces noires
eg_Black_King_Scores = [[20, 30, 10, 0, 0, 10, 30, 20],
                        [20, 20, 0, 0, 0, 0, 20, 20],
                        [-10, -20, -20, -20, -20, -20, -20, -10],
                        [-20, -30, -30, -40, -40, -30, -30, -20],
                        [-30, -40, -40, -50, -50, -40, -40, -30],
                        [-30, -40, -40, -50, -50, -40, -40, -30],
                        [-30, -40, -40, -50, -50, -40, -40, -30],
                        [-30, -40, -40, -50, -50, -40, -40, -30]]

Black_Pawn_Scores = [[0, 0, 0, 0, 0, 0, 0, 0],
                     [5, 10, 10, -20, -20, 10, 10, 5],
                     [5, -5, -10, 0, 0, -10, -5, 5],
                     [0, 0, 0, 20, 20, 0, 0, 0],
                     [5, 5, 10, 25, 25, 10, 5, 5],
                     [10, 10, 20, 30, 30, 20, 10, 10],
                     [50, 50, 50, 50, 50, 50, 50, 50],
                     [0, 0, 0, 0, 0, 0, 0, 0]
                     ]

Black_knight_Scores = [[-50, -40, -30, -30, -30, -30, -40, -50],
                       [-40, -20, 0, 5, 5, 0, -20, -40],
                       [-30, 5, 10, 15, 15, 10, 5, -30],
                       [-30, 0, 15, 20, 20, 15, 0, -30],
                       [-30, 5, 15, 20, 20, 15, 5, -30],
                       [-30, 0, 10, 15, 15, 10, 0, -30],
                       [-40, -20, 0, 0, 0, 0, -20, -40],
                       [-50, -40, -30, -30, -30, -30, -40, -50]]

Black_Bishop_Scores = [[-20, -10, -10, -10, -10, -10, -10, -20],
                       [-10, 5, 0, 0, 0, 0, 5, -10],
                       [-10, 10, 10, 10, 10, 10, 10, -10],
                       [-10, 0, 10, 10, 10, 10, 0, -10],
                       [-10, 5, 5, 10, 10, 5, 5, -10],
                       [-10, 0, 5, 10, 10, 5, 0, -10],
                       [-10, 0, 0, 0, 0, 0, 0, -10],
                       [-20, -10, -10, -10, -10, -10, -10, -20]]

Black_Rook_Scores = [[0, 0, 0, 5, 5, 0, 0, 0],
                     [-5, 0, 0, 0, 0, 0, 0, -5],
                     [-5, 0, 0, 0, 0, 0, 0, -5],
                     [-5, 0, 0, 0, 0, 0, 0, -5],
                     [-5, 0, 0, 0, 0, 0, 0, -5],
                     [-5, 0, 0, 0, 0, 0, 0, -5],
                     [5, 10, 10, 10, 10, 10, 10, 5],
                     [0, 0, 0, 0, 0, 0, 0, 0]]


Black_Queen_Scores = [[-20, -10, -10, -5, -5, -10, -10, -20],
                      [-10, 0, 5, 0, 0, 0, 0, -10],
                      [-10, 5, 5, 5, 5, 5, 0, -10],
                      [0, 0, 5, 5, 5, 5, 0, -5],
                      [-5, 0, 5, 5, 5, 5, 0, -5],
                      [-10, 0, 5, 5, 5, 5, 0, -10],
                      [-10, 0, 0, 0, 0, 0, 0, -10],
                      [-20, -10, -10, -5, -5, -10, -10, -20]]

# *****************************************************************************************************************************************************************************
piecePosition = {"wN": White_knight_Scores,
                 "bN": Black_knight_Scores,
                 "wQ": White_Queen_Scores,
                 "bQ": Black_Queen_Scores,
                 "wB": White_Bishop_Scores,
                 "bB": Black_Bishop_Scores,
                 "wR": White_Rook_Scores,
                 "bR": Black_Rook_Scores,
                 "wP": White_Pawn_Scores,
                 "bP": Black_Pawn_Scores,
                 "bK": eg_Black_King_Scores,
                 "wK": eg_White_King_Scores}


# *****************************************************************************************************************************************************************************

def findRandomMove(validMoves):
    return validMoves[random.randint(0, len(validMoves) - 1)]


# *****************************************************************************************************************************************************************************
# fait appelle à la fonction findMoveNegaMax et retourne le "meilleur" mouvement
def findBestMove(gs, validMoves):
    global nextMove
    nextMove = None  # reset nextMove to none before call this method
    findMoveNegaMax(gs, validMoves, DEPTH, -CHECKMATE, CHECKMATE, 1 if gs.whiteToMove else -1)
    return nextMove


# *****************************************************************************************************************************************************************************
# construit un arbre de recherche et évalue chacun de ses nœuds avec la fonction d'évaluation
def findMoveNegaMax(gs, validMoves, depth, alpha, beta, turnMultiplier):
    global nextMove
    if depth == 0:
        return turnMultiplier * scoreBoard(gs)

    maxScore = -CHECKMATE
    for move in validMoves:
        gs.makeMove(move)
        nextMoves = gs.getValidMoves()
        score = -findMoveNegaMax(gs, nextMoves, depth - 1, -beta, -alpha, -turnMultiplier)
        # score = max(score,maxScore)
        if score > maxScore:
            maxScore = score
            if depth == DEPTH:
                nextMove = move
        gs.undoMove()
        if maxScore > alpha:  # pruning happens
            alpha = maxScore
        if alpha >= beta:
            break

    return maxScore


# *****************************************************************************************************************************************************************************
# cette fonction est la fonction d'évaluation, elle utilise le score de la position dans l'échiquier et la valeur de la pièce pour évaluer un mouvment
def scoreBoard(gs):
    if gs.checkMate:
        if gs.whiteToMove:
            return -CHECKMATE  # black wins
        else:
            return CHECKMATE  # white wins
    elif gs.staleMate:
        return STALEMATE

    score = 0
    for row in range(len(gs.board)):
        for col in range(len(gs.board)):
            square = gs.board[row][col]
            if square != "--":
                PositionScore = piecePosition[square][row][col]
                if square[0] == 'w':
                    score += pieceScore[square[1]] * .1 + PositionScore
                elif square[0] == 'b':
                    score -= pieceScore[square[1]] * .1 + PositionScore

    return score
