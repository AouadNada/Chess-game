# classe pour recevoir les inputs des mouvements

class Move:
    def __init__(self, startSq, endSq, board,isCastleMove=False):
        # startsq fait reference à la case de la piece qui va bouger
        self.startSq = startSq
        self.endSq = endSq
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        # endsq fait reference à la case ou la piece va bouger
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        # pieceMoved stocke la piece qui va bouger
        self.pieceMoved = board[self.startRow][self.startCol]
        # pieceCaptured stocke la piece qui va être capturer
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.isCastleMove = isCastleMove
        # variable pour verifier s'il s'agit d'une promotion du pion
        self.isPawnPromotion = False
        self.isPawnPromotion = (self.pieceMoved == "wP" and self.endRow == 0) or (self.pieceMoved == "bP" and self.endRow == 7)

        self.moveID = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol

    # deux fonctions pour traduire les mouvements sur ecrans en notations d'échec

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID


