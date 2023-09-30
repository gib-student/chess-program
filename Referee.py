import Board

class Referee:
    def valid_move(self, board=Board.Board(), move=""):
        moves = move.split(" to ")
        # Split move into start and destination squares
        initial = moves[0]
        destination = moves[1]
        # Ensure each move has two characters, no more and no less
        if self.has_2_chars(initial, destination):
            # Split each move into column and row
            initial_column  = list(initial)[0]
            initial_row     = list(initial)[1]
            destination_column  = list(destination)[0]
            destination_row     = list(destination)[1]
        




        # Identify the color of the squares 

        # Identify the piece on the squares

        # Ensure the move is legal for the given piece


        # Ensure that the destination square does not contain a piece
        # of the same color as the starting square

    # Ensure the string contains a letter a-h and a number 1-8.
    # Expects a string.
    # Returns true if input is valid, and false if it is not.
    def valid_move_input(self, move):
        # Split each move into letter and number
        first_char = list(move)[0]
        second_char = list(move)[0]
        column = first_char     # default: first char is column
        row = second_char       # default: second char is row
        

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