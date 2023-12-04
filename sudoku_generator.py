# Structure and ideas came from https://github.com/zhoulisha/Sudoku-Project

import math, random

class SudokuGenerator:
  
  def __init__(self, removed_cells, row_length = 9): # Constructor for the SudokuGenerator class.
    self.row_length = row_length # the length of each row is 9
    self.removed_cells = removed_cells # the total number of cells to be removed is set as removed_cells depending on the difficulty level
    self.board = [[0 for i in range(row_length)] for j in range(row_length)] # the board is represented as a 2D list of 0s with the length of the rows and columns set to row_length
    self.box_length = math.sqrt(int(row_length)) # the length of each box is set as the square root of row_length  

  def get_board(self): # Returns a 2D python list of numbers, which represents the board
    return self.board

  def print_board(self): # Displays the board to the console.
    for row in self.board: # this iterates through each row in the board
      print(row) # this prints each row that was iterated in the loop

  def valid_in_row(self, row, num): # Determines if num is contained in the given row (horizontal) of the board
    for i in range(self.row_length): # this iterates through each column in the row
      if self.board[row][i] == num: # this checks if the value in the box is equal to the specified number
        return False #if num is already in the specificed row, then num is not valid
      return True # if num is not in the specified row, then num is valid

  def valid_in_col(self, col, num): # Determines if num is contained in the given column(vertical) of the board
    for i in range(self.row_length): # this iterates through each row in the column
      if self.board[i][col] == num: # this checks if the value in the box is euqal to the specified number
        return False # if num is already in the specified column, then num is not valid
      return True # if num is not in the specified column, then num is valid

  def valid_in_box(self, row_start, col_start, num): # Determines if num is contained in the 3x3 box from specified on the board
    for i in range(row_start, col_start): # this iterates through the each row and column in the list
      for j in range(row_start + 2, col_start + 2): # this iterates through each 3x3 box in the list
        if self.board[i + row_start][j + col_start] == num: # this checks to see if the value in the box is equal to a specified number
          return False # if num is in the specified box, then num is not valid
    return True # if num is not in the specified box, then num is valid 

  def is_valid(self, row, col, num): # Returns if it is valid to enter num at (row, col) in the board by checking the appropriate row, column, and box
    if self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row - row % 3, col - col % 3, num): # this checks to see if the num is valid in the row, column, and box for each 3x3 box
      return True # if num is valid, then num will be added to the specified box
    return False # if num is not valid, then num will not be added to the specified box

  def fill_box(self, row_start, col_start): # Fills the specified 3x3 box with values by generating a rando digit which has not been used in the box
    for i in range(row_start, col_start): # this iterates through the entire 2D list
      for j in range(row_start + 2, col_start + 2): # this iterates through each 3x3 box in the list
        self.board[i][j] = random.randint(1, 9) # this randomly adds a values into the specified box

  def fill_diagonal(self): # Fills the three boxes along the main diagonal of the board
    for i in range(0, self.row_length, 3): # this iterates through each row by 3
      self.fill_box(i, i) # this fills the 3x3 box in the main diagonal
      
  def fill_remaining(self, row, col):  # Fills the remaining cells in the board to create the solution
    if col >= self.row_length and row < self.row_length - 1: # this checks to see if the column is greater than or equal to the row length and if the row is less than the row length
        row += 1 # row increments by 1
        col = 0 # col is set to 0
    if row >= self.row_length and col >= self.row_length: # this checks to see if the row is greater than or equal to the row length and if the column is greater than or equal to
        return True # if the row and column are greater than or equal to the row length, then the board is filled
    if row < self.box_length: # this checks if the row is less than the box length
        if col < self.box_length: # this checks if the col is less than the box length
            col = self.box_length # col is set to the length of the boxes
    elif row < self.row_length - self.box_length: # this checks if the row is less than the row length minus the box length
        if col == int(row // self.box_length * self.box_length): # this checks if the col is equal to the row divided by the box length times the box length
            col += self.box_length # col increments by the length of the boxes
    else:
        if col == self.row_length - self.box_length: # this checks if the col is equal to the row length minus the box length
            row += 1 # row increments by 1
            col = 0 # row is set to 0
            if row >= self.row_length: # this checks to see if the row is greater than or equal to the row length
                return True # if the row is greater than or equal to the row length, then the board is filled
              
    for num in range(1, self.row_length + 1): # this iterates through each value in the board
        if self.is_valid(row, col, num): # if the value is not in the specified box
            self.board[row][col] = num # the value is added to the specified box
            if self.fill_remaining(row, col + 1): # this checks to see if the entire row is filled
                return True # if the entire row board is filled, then it will move on to the next row
    return False

  def fill_values(self): # Constructs a solution by calling fill_diagonal and fill_remaining
    self.fill_diagonal() # fills the main diagonal boxes of the board
    self.fill_remaining(0, self.box_length) # add values to any empty boxes in the board

  def remove_cells(self): # Removes the appropriate number of cells in the board by setting some values to 0
    while self.removed_cells > 0: # this loops through until every specified cell is removed
      row = random.randint(0, self.row_length - 1) # this randomly selects a row
      col = random.randint(0, self.row_length - 1) # this randomly selects a column
      if self.board[row][col] != 0: # this checks to see if the value in the box is not 0
        self.board[row][col] = 0 # if the value is not 0, then the value in the box is set to 0
        self.removed_cells -= 1 # the number of cells that needs to be removed decreases by 1

  def generate_sudoku(size, removed): # Creates A sudoku generator and filles the board with values, removes the appropraite number of cells, and returns the board and its solution
    sudoku = SudokuGenerator(size, removed) # this initates the sudoku generator
    sudoku.fill_values() # this calls fill_values to add values to the sudoku board
    board = sudoku.get_board() # this prints out the given board
    sudoku.remove_cells() # this removes the specified number of cells from the board
    board = sudoku.get_board() # this prints the new board
    return board
