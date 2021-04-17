from pieces.pieces import *
from colors import COLOR
class Moves:
    def __init__(self,board):
        self.board = board
    
    def generate_moves(self) -> dict:
        """
        Generate move for each piece of player
        Return dictionary with piece position as a key and list of possible moves as items
        """
        moves = {}  
        for row in self.board:
            for square in row:
                piece = square.piece
                fig ={
                    Pawn:self.pawn_move,
                    Bishop:self.bishop_move,
                    Rook:self.rook_move,
                    Knight:self.knight_move,
                    King:self.king_move,
                    Queen:self.queen_move
                }
                if isinstance(piece,Piece):
                    m = fig.get(type(piece))(piece.row, piece.col)
                    if not len(piece.pinnedby):
                        moves[piece.row, piece.col] = m
                    elif len(piece.pinnedby) == 1:
                        if piece.pinnedby[0] in m:
                            moves[piece.row, piece.col] = piece.pinnedby[0]
                    else:
                        continue
                else:
                    continue
        return moves

    def move(self):
        pass
    
    def pin(self):
        pass

    def pawn_move(self,row,col):
        s =  -1 if self.board[row][col].piece.color == COLOR.White else 1
        r =  3 if self.board[row][col].piece.touched else 2
        move = []
        for x in range(1,r+1):
            if not row + x*s in range(8):
                break
            if  not self.board[row + x*s][col].piece:
                move.append([row + x*s, col])
            else:
                break
        for x in [-1,1]:
            if not row + 1*s in range(8) or not col + x in range(8):
                continue
            if  self.board[row + 1*s][col + x].piece:
                move.append([row + 1*s, col + x])
                self.board[row + 1*s][col + x].isOccupied = True
        return move

    def knight_move(self, row, col):
        move = []
        possible = [[-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2]]
        for x, y in possible:
            if row + x in range(8) and col + y in range(8):
                if not self.board[row + x][col + y].piece and not self.board[row + x][col + y].isOccupied :
                    move.append([row + x, col + y])
                elif (self.board[row + x][col + y].piece.color != self.board[row][col].piece.color and 
                     not self.board[row + x][col + y].isOccupied):
                     move.append([row + x, col + y])
        return move

    def bishop_move(self, row, col):
        move = []
        for x,y in [[1,1], [-1,-1], [1,-1], [-1,1]]:
            for i in range(1,8):
                if not row + i*x in range(8) or not col + i*y in range(8):
                    break
                if self.board[row + i*x][col + i*y].piece:
                    if self.board[row + i*x][col + i*y].piece.color != self.board[row][col].piece.color:
                        move.append([row + i*x, col + i*y])
                    break
                else:
                    move.append([row + i*x, col + i*y])
        return move

    def rook_move(self, row, col):
        move = []
        for x,y in [[0,1], [0,-1], [1,0], [-1,0]]:
            for i in range(1,8):
                if not row + i*x in range(8) or not col + i*y in range(8):
                    break
                if self.board[row + i*x][col + i*y].piece:
                    if self.board[row + i*x][col + i*y].piece.color != self.board[row][col].piece.color:
                        move.append([row + i*x, col + i*y])
                    break
                else:
                    move.append([row + i*x, col + i*y])
        return move

    def queen_move(self, row, col):
        move = []
        move += self.rook_move(row,col)
        move += self.bishop_move(row,col)
        return move

    def king_move(self, row, col):
        move = []
        possible = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        for x, y in possible:
            if row + x in range(8) and col + y in range(8):
                if not self.board[row + x][col + y].piece and not self.board[row + x][col + y].isOccupied :
                    move.append([row + x, col + y])
                elif (self.board[row + x][col + y].piece.color != self.board[row][col].piece.color and 
                     not self.board[row + x][col + y].isOccupied):
                     move.append([row + x, col + y])
        return move