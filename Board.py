from pieces.pieces import *
from Square import Square

class Board(object):
    startFEN = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
    def __init__(self) -> None:
        super().__init__()
        self.board = [[Square(x,y) for x in range(8)] for y in range(8)]
    def load_fen(self,fen):
        color = lambda p : 'White' if p.islower() else 'Black'
        piece = {'p': Pawn,'n':Knight,'r':Rook, 'b':Bishop, 'q':Queen, 'k':King}
        row = 7
        col = 0
        for char in fen:
            if char == '/':
                row -= 1
                col = 0
            elif char.isnumeric():
                col += int(char)
            else:
                self.board[row][col].piece = piece.get(char.lower())(color(char),col,row)
                col += 1
            
    def generate_fen(self):
        pass

    def __repr__(self) -> str:
        out = ""
        for row in self.board:
            for s in row:
                if s.piece:
                    out += str(s.piece) + "  "
                else:
                    out +=" "
            out += "\n"
        return out


b = Board()
b.load_fen(Board.startFEN)
print(b)

print(b.board[7][0].piece.color)