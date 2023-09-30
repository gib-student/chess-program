class Move:
   def __init__(self, initial, destination, initial_column, initial_row,
                destination_column, destination_row):
      self.starting_square = initial
      self.destination_square = destination
      
      self.initial_column = initial_column
      self.initial_row = initial_row
      self.destination_column = destination_column
      self.destination_row = destination_row
