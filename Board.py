import Square

# Starting chess board with its associated pieces
class Board:

    # A board will be a collection of squares
    def __init__(self):
        self.squares    = {}
        self.columns    = ["a", "b", "c", "d", "e", "f", "g", "h"]
        self.rows       = ["1", "2", "3", "4", "5", "6", "7", "8"]
        self.black_pieces = ["br", "bn", "blb", "wq", "wk", "bdb", "bn", "br"]
        self.white_pieces = ["wr", "wn", "wdb", "wq", "wk", "wlb", "wn", "wr"]

        # Create array of squares
        color = "white" # a1 is black (will get flipped)
        # Board will be ordered first by columns...
        for column in self.columns:
            # Create a dictionary for each column
            col_list = {}
            # then by rows.
            
            # Create a square for each row in the column
            for row in self.rows:
                # assign piece
                piece = ""
                piece_index = self.columns.index(column)
                # If the piece is in the 1st row, it will be a white 
                # power piece
                if row == "1":
                    piece = self.white_pieces[piece_index]
                # If the piece is in the 2nd row, it will be a white pawn
                elif row == "2":
                    piece = "wp"
                # If the piece is in the 7th row, it will be a black pawn
                elif row == "7":
                    piece = "bp"
                # If the piece is in the 8th row, it will be a black
                # power piece
                elif row == "8":
                    piece = self.black_pieces[piece_index]

                # alternate color
                color = "black" if color == "white" else "white"

                # Create square
                square = Square(column, row, color, piece)
                # then add to array.
                col_list[row] = square
            # Add column to board
            self.squares[column] = col_list
