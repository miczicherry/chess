from pieces.pieces import *

class Moves:
    def __init__(self,board):
        self.board = board
    
    def generate_moves(self):
        """Generate move for each piece of player"""
        moves = {}
        for square in self.board:
            piece = square.piece
            if not piece:
                continue
            elif isinstance(piece, Pawn):
                m = self.pawn_move()
                if not len(piece.pinnedby):
                    moves[[piece.col, piece.row]] = m
                elif len(piece.pinnedby) == 1:
                    if piece.pinnedby[0] in m:
                        moves[[piece.col, piece.row]] = piece.pinnedby[0]
                else:
                    continue
            elif isinstance(piece, Bishop):
                m = self.bishop_move()
                if not len(piece.pinnedby):
                    moves[[piece.col, piece.row]] = m
                elif len(piece.pinnedby) == 1:
                    if piece.pinnedby[0] in m:
                        moves[[piece.col, piece.row]] = piece.pinnedby[0]
                else:
                    continue
            
    def move(self):
        pass
    
    def pin(self):
        pass

    def pawn_move(self,col,row):
        pass

    def knight_move(self,col,row):
        pass

    def bishop_move(self,col,row):
        pass

    def rook_move(self, col, row):
        pass

    def queen_move(self, col, row):
        pass
    
    def king_move(self, col, row):
        pass
