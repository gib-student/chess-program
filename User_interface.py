import Board
import Referee
import Move

class User_interface:
    def __init__(self):
        self.referee = Referee.Referee()

    # Main game menu
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
        response = response.upper()

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
            response = response.upper()

    def play_chess(self, board=Board.Board(), turn="white"):
        done = False
        # Game loop
        while not done:
            # Prompt for white's move and edit board
            if turn == "white":
                new_move = Move.Move()
                # Opening message
                print("White's turn.")
                # Get initial square
                starting_square     = self.get_square(new_move, "initial")
                destination_square  = ""
                
                # Get destination square
                if starting_square != "quit":
                    # Once we have the starting square, get the destination square
                    destination_square = self.get_square(new_move, "destination")
                    
                # Quit if user wants to end the game
                else: done = True

            # Prompt for black's move and edit board
            elif turn == "black":
                new_move = Move.Move()
                # Opening message
                print("Black's turn.")

        # Check if user wants to save the game before we quit

    # Get valid input from the user
    def get_square(self, new_move, initial_or_dest):
        response     = ""
        square_valid = ""
        # Keep prompting for input until they give a valid square, or 
        # they want to quit
        while square_valid != "valid" and not self.should_quit(response):
            # Prompt for square
            if initial_or_dest == "initial":
                response = input("Starting square: ")
            elif initial_or_dest == "destination":
                response = input("Destination square: ")

            # Check to ensure input matches to a square
            square_valid = self.referee.valid_square(response, new_move, initial_or_dest)
            
            # If not, case test, and prompt for input again.
            if square_valid != "valid":
                # only one char provided
                if square_valid == "not enough chars": 
                    print("Please enter a column (a-h) and a row (1-8). i.e. a1")
                # too many chars
                elif square_valid == "too many chars":
                    print("Please enter one letter (a-h) for a column, and one number (1-8) for a row. i.e. a1")
                # correct number of chars, but invalid input
                elif square_valid == "invalid square":
                    print("Invalid square. Enter a letter (a-h) for a column, and a number (1-8) for a row. i.e. a1")

        # If the user wants to quit, return "quit"
        if self.should_quit(response): return "quit"
        # otherwise, return the valid response
        else: return response
    
    # Handle user input
    def handle_input(self, new_move):
        pass


    # Return true if user wants to quit, false if they do not
    def should_quit(self, response): 
        # Lowercase response
        response = response.lower()
        return response == "q" or response == "quit"
    
    def start_loaded_game(self, filename=""):
        board = Board()