import Board

class User_interface:
    def play_chess(self, board=Board.Board(), turn="white"):
        response = ""
        # Game loop
        while response != "Q":
            if turn == "white":
                response = input("White's turn. What is move? --> (i.e. a1 to h8)")
                # Make sure move is valid

            elif turn == "black":
                response = input("Black's turn. What is move? --> (i.e. a1 to h8)")
                # Make sure move is valid
    
    def start_loaded_game(self, filename=""):
        board = Board()

    def display_menu(self):
        # Game menu
        print()
        print("Welcome to Spoken Chess!")
        print()
        print("Game Menu")
        print("[N]ew game")
        print("[L]oad Game")
        print("[Q]uit")
        response = input("--> ")

        # Keep playing chess until they quit
        while response != "Q":
            if response == "N":
                self.play_chess()
            elif response == "L":
                filename = input("What is the name of chess game file?")
                self.start_loaded_game(filename)
            
            # After they play the game, display the menu again
            print()
            print("Game Menu")
            print("[N]ew game")
            print("[L]oad Game")
            print("[Q]uit")
            response = input("--> ")
    
    def valid_move(self, board=Board.Board(), move=""):
        moves = move.split(" to ")
        # Split move into start and destination squares
        start = moves[0]
        destination = moves[1]
        # Split each move into letter and number
        start_letter = list(start)[0]
        # Ensure first character is a letter
        if 'A' > start_letter > 
        # Identify the color of the squares 
        color = board.squares
        # Identify the piece on the squares

        # Ensure the move is legal for the given piece


        # Ensure that the destination square does not contain a piece
        # of the same color as the starting square
