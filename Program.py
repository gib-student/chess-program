# Chess program

# Square on the board
class Square:
    # A square will have a row and a column
    def __init__(self, row="", column=0):
        self.row = row
        self.column = column

# Chess board
class Board:
    # A board will be a collection of squares
    def __init__(self):
        self.board = []
        rows    = ["A", "B", "C", "D", "E", "F", "G", "H"]
        columns = [1, 2, 3, 4, 5, 6, 7, 8]
        for row in rows:
            for column in columns:
                square = Square(row, column)
                self.board.append(square)

# Create a board
board = Board()