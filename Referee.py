import Board

# Referee class
class Referee:
    def valid_move(self, board=Board.Board(), move=""):
        moves = move.split(" to ")
        # Split move into start and destination squares
        initial = moves[0]
        destination = moves[1]

        # Identify the color of the squares 

        # Identify the piece on the squares

        # Ensure the move is legal for the given piece


        # Ensure that the destination square does not contain a piece
        # of the same color as the starting square

    # Ensure the string contains a letter a-h and a number 1-8.
    # Expects a string.
    # Returns true if input is valid, and false if it is not.
    def valid_square(self, input, move_object, initial_or_dest):
        # Check if input has at least two chars
        if len(list(input)) < 2:
            return "not enough chars"
        # Check if input has more than two chars
        elif len(list(input)) > 2:
            return "too many chars"
        # Check if input corresponds to a square on the board
        # Split each move into letter and number
        column  = ""
        row     = ""
        char1 = list(input)[0]
        char2 = list(input)[1]
        # Figure out which char is the letter (column), and which is the
        # row (number)
        # Check if char1 corresponds to a letter a-h
        if 'a' <= char1 <= 'h':
            column = char1
            # Check if char2 corresponds to a number 1-8
            if '1' <= char2 <= '8':
                row = char2
            # if not, invalid square
            else: return "invalid square"
        # if not, check if char2 corresponds to a letter a-h
        elif 'a' <= char2 <= 'h':
            column = char2
            # Check if char1 corresponds to a number 1-8
            if '1' <= char1 <= '8':
                row = char1
            else: return "invalid square"
        # if not, invalid square
        else: return "invalid square"

        # Once all tests are passed, assign values in the move object
        # and return "valid"
        if initial_or_dest == "initial":
            move_object.initial         = input
            move_object.initial_column  = column
            move_object.initial_row     = row
        elif initial_or_dest == "destination":
            move_object.destination         = input
            move_object.destination_column  = column
            move_object.destination_row     = row
        return "valid"
        

    # Ensure input is a number 1-8.
    # Returns true if input is a number 1-8, and false if it is not.
    def number_1_through_8(self, number):
        return '1' <= number <= '8'
    
    # Ensure input is a letter A-H.
    # Returns true if input is a letter A-H, and false if it is not.
    def letter_A_through_H(self, letter):
        return 'A' <= letter <= 'H' or 'a' <= letter <= 'h'
    
    # Ensure move has two characters
    def has_2_chars(self, move1, move2):
        return len(move1) == 2 and len(move2) == 2