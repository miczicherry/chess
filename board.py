from pieces.pieces import *
from square import Square
from colors import COLOR
from move import Moves
class Board(object):
    startFEN = "rnbqkbnr/pppppppp/8/8/5n2/8/PPPPPPPP/RNBQKBNR"
    def __init__(self) -> None:
        super().__init__()
        self.board = [[Square(x,y) for x in range(8)] for y in range(8)]
    def load_fen(self,fen):
        color = lambda p : COLOR.White if p.islower() else COLOR.Black
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
                    out += str(s.piece) + " "
                else:
                    out +="  "
            out += "\n"
        return out


b = Board()
b.load_fen(Board.startFEN)
print(b)
m = Moves(b.board)
mv = m.generate_moves()
for r in mv:
    print(r ,mv[r])

for x,y in mv[3,5]:
    b.board[x][y].piece = '.'

print(b)