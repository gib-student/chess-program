# Square on the board
class Square:
    # A square will have a row and a column
    def __init__(self, column="", row=0, color="none", piece = ""):
        self.column     = column
        self.row        = row
        self.color      = color
        self.piece      = piece
