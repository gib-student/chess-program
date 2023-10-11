# Each move has a starting (initial) square, a destination square, which
# both are organized into rows and columns; it also has a piece, piece
# color, and whether or not it captured another piece; if it did, then
# the captured piece is recorded.
class Move:
   def __init__(self, initial="", destination="", initial_column="", initial_row="",
                destination_column="", destination_row="", piece="", piece_color="",
                capture=False, captured_piece=""):
      
      self.starting_square       = initial
      self.destination_square    = destination
      self.initial_column        = initial_column
      self.initial_row           = initial_row
      self.destination_column    = destination_column
      self.destination_row       = destination_row
      self.piece                 = piece
      self.piece_color           = piece_color
      self.capture               = capture
      self.captured_piece        = captured_piece