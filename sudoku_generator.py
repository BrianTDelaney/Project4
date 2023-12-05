# Structure and ideas came from https://github.com/zhoulisha/Sudoku-Project and python library

import math, random

class SudokuGenerator:

  def __init__(self, row_length, removed_cells): # Constructor for the SudokuGenerator class.
    self.row_length = 9
    self.removed_cells = removed_cells
    self.board = [[0 for i in range(row_length)] for j in range(row_length)] 
    self.box_length = int(math.sqrt(int(row_length))) 

  def get_board(self): # Returns a 2D python list of numbers, which represents the board
    return self.board

  def print_board(self): # Displays the board to the console.
    for row in self.board:
      print(row) 

  def valid_in_row(self, row, num): # Determines if num is contained in the given row (horizontal) of the board
    for i in range(self.row_length): 
      if self.board[row][i] == num: 
        return False 
    return True 

  def valid_in_col(self, col, num): # Determines if num is contained in the given column(vertical) of the board
    for i in range(self.row_length):
      if self.board[i][col] == num:
        return False 
    return True 

  def valid_in_box(self, row_start, col_start, num): # Determines if num is contained in the 3x3 box from specified on the board
    for row in range(row_start, row_start + 3):
      for col in range(col_start, col_start + 3):
        if self.board[row][col] == num: 
            return False 
    return True 

  def is_valid(self, row, col, num): # Returns if it is valid to enter num at (row, col) in the board by checking the appropriate row, column, and box
    if self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row - row % 3, col - col % 3, num): 
      return True 
    return False 

  def unused_in_box(self, row_start, col_start, num):
    for row in range(row_start, row_start + 3):
        for col in range(col_start, col_start + 3):
            if self.board[row][col] == num:
                return False
    return True

  def fill_box(self, row_start, col_start): # Fills the specified 3x3 box with values by generating a random digit which has not been used in the box
    nums = [int(i + 1) for i in range(self.row_length)]
    nums = random.sample(nums, len(nums))
    for i in range(self.box_length):
        for j in range(self.box_length):
            row = row_start + i
            col = col_start + j
            for num in nums:
                if self.unused_in_box(row_start, col_start, num):
                    self.board[row][col] = num
                    nums.remove(num)
                    break

  def fill_diagonal(self): # Fills the three boxes along the main diagonal of the board
    for i in range(0, self.row_length, 3): 
      for j in range(0, self.row_length, 3): 
        self.fill_box(i, j) 

  def fill_remaining(self, row, col):  # Fills the remaining cells in the board to create the solution
    if col >= self.row_length and row < self.row_length - 1: 
        row += 1 
        col = 0 
    if row >= self.row_length and col >= self.row_length: 
        return True 
    if row < self.box_length: 
        if col < self.box_length: 
            col = self.box_length 
    elif row < self.row_length - self.box_length:
        if col == int(row // self.box_length * self.box_length): 
            col += self.box_length 
    else:
        if col == self.row_length - self.box_length: 
            col = 0 
            if row >= self.row_length: 
                return True 

    for num in range(1, self.row_length + 1):
        if self.is_valid(row, col, num):
            self.board[row][col] = num 
            if self.fill_remaining(row, col + 1): 
                return True 
    return False

  def fill_values(self): # Constructs a solution by calling fill_diagonal and fill_remaining
    self.fill_diagonal() 
    self.fill_remaining(0, self.box_length) 

  def remove_cells(self): # Removes the appropriate number of cells in the board by setting some values to 0
    while self.removed_cells > 0:
      row = random.randint(0, self.row_length - 1) 
      col = random.randint(0, self.row_length - 1) 
      if self.board[row][col] != 0: 
        self.board[row][col] = 0 
        self.removed_cells -= 1

def generate_sudoku(size, removed): # Creates A sudoku generator and filles the board with values, removes the appropriate number of cells, and returns the board and its solution
    sudoku = SudokuGenerator(size, removed) 
    sudoku.fill_values() 
    board = sudoku.get_board() 
    sudoku.remove_cells()
    board = sudoku.get_board() 
    return board
