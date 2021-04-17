class Piece(object):
    def __init__(self, color, col, row):
        super(Piece, self).__init__()
        self.color = color
        self.touched = False
        self.row = row
        self.col = col
        self.pinnedby = []
