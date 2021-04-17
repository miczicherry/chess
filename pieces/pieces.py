from pieces.Piece import Piece


class Pawn(Piece):
    img_src = ""
    weight = 1
    
    def __init__(self, color, col, row) -> None:
        super().__init__(color, col, row)
        
    def __str__(self) -> str:
        return "p"


class Knight(Piece):
    img_src = ""
    weight = 3
    
    def __init__(self, color, col, row) -> None:
        super().__init__(color, col, row)
        
    def __str__(self) -> str:
        return "n"


class Bishop(Piece):
    img_src = ""
    weight = 3

    def __init__(self, color, col, row) -> None:
        super().__init__(color, col, row)
        
    def __str__(self) -> str:
        return "b"


class Rook(Piece):
    img_src = ""
    weight = 5

    def __init__(self, color, col, row) -> None:
        super().__init__(color, col, row)
    
    def __str__(self) -> str:
        return "r"


class Queen(Piece):
    img_src = ""
    weight = 9

    def __init__(self, color, col, row) -> None:
        super().__init__(color, col, row)

    def __str__(self) -> str:
        return "q"

class King(Piece):
    img_src = " "
    weight = 0
    
    def __init__(self, color, col, row) -> None:
        super().__init__(color, col, row)
        
    def __str__(self) -> str:
        return "k"
