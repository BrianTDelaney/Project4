# Project 4: Sudoku Generator
# Structure and ideas came from python libary and https://github.com/zhoulisha/Sudoku-Project

import math, random


class SudokuGenerator:
    def __init__(self, row_length, removed_cells): # Constructor for the SudokuGenerator class. 
        self.row_length = row_length # length of each row and column is always 9
        self.removed_cells = removed_cells # the total number of cells to remove is dependent on the difficulty level
        self.board = [[0 for row in range(self.row_length)] for col in range(self.row_length)] # creates a 2D list of integers to represent the board
        self.box_length = int(math.sqrt(self.row_length)) # the length of each cell is always 3

    def get_board(self): # Returns a 2D list of integers which represents the board
        return self.board

    def print_board(self): # Displays the board to the console
        for row in self.board: # this iterates through every row in the board
          print(row) # this prints every row in the board

    def valid_in_row(self, row, num): # Determines if num is contained in the specified row (horizontal) of the board
        if num in self.board[row]: # this checks if a value is in the specified row
          return False # if num is in the specified row, then it not valid
        else:
          return True # if num is not in the specified row, then it is valid

    def valid_in_col(self, col, num): # Determines if num is contained in the specified column (vertical) of the board
        for row in range(self.row_length): # this iterates through every row in the board
            if self.board[row][col] == num: # this checks if a value is at a specific columns
                return False # if the value is in the specified column, then it is not valid
        return True # if the value is not in the specified column, then it is valid

    def valid_in_box(self, row_start, col_start, num): # Determines if the num contained in the 3x3 box specified on the board
        for row in range(self.box_length): # this iterates through every row in a specified box
            for col in range(self.box_length): # this iterates through every column in a specified box
                if self.board[row_start + row][col_start + col] == num: # this checks if the value is in the specified box
                    return False # if the value is in the specified box, then it is not valid
        return True # if the value is not in the specified box, then it is valid

    def is_valid(self, row, col, num): # Determines if a value is valid to be placed at (row, col) in the board
        return self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row - row % self.box_length, col - col % self.box_length, num) # this checks if all the valid methods are satisifed in order to return the value to the board

    def unused_in_box(self, row_start, col_start, num): # Determines if a value is not used in a 3x3 box specified on the board
        for row in range(row_start, row_start + self.box_length): # this iterates through every row in the board
            for col in range(col_start, col_start + self.box_length): # this iterates through every column in the board
                if self.board[row][col] == num: # this checks if a value is in a specified box
                    return False # if the value is in the specified box, then it is not valid
        return True # if the value is not in the specified box, then it is valid

    def fill_box(self, row_start, col_start): # Fills the specified 3x3 box with values
        sudoku_values = [i + 1 for i in range(self.row_length)] # this creates a list of values from 1 to 9
        sudoku_values = random.sample(sudoku_values, len(sudoku_values)) # this randomizes the list of values for the sudoku board
        for i in range(self.box_length): # this iterates through each row in a specified box
            for j in range(self.box_length): #this iterates to each column in a specified box
                row = row_start + i # this establisheds a row that will be used to place a value in the specified box
                col = col_start + j # this establishes a column that will be used to place a value in the specified box
                for values in sudoku_values: # this iterates through a list of numbers between 1-9
                    if self.unused_in_box(row_start, col_start, sudoku_values): # this checks if the value is used in the specified box
                        self.board[row][col] = values # if the value is not used in a specified box, then it will be added to the board
                        sudoku_values.remove(values) # this removes the current value, so it does not repeat in the same box
                        break

    def fill_diagonal(self): # Fills the three boxes along the main diagonal of the board
        for i in range(0, self.row_length, self.box_length): # this iterates through each box in a diagonal order
            self.fill_box(i, i) # specified boxes are filled at (0,0), (3,3), and (6,6)

    def fill_remaining(self, row, col):  # Fills the remaining cells in the board to create the solution
        ''' 
        this checks through each row and column in the sudoku board to set a up the process of filling the empty cells with values 
        '''
        if (col >= self.row_length and row < self.row_length - 1):
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
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1): # this iterates through each number between 1-9
            if self.is_valid(row, col, num): # this checks if the value is used in the row and col
                self.board[row][col] = num # if the value is unused, then it will be added to the board at the specified cell
                if self.fill_remaining(row, col + 1): # this iterates through each cell in a row to determine if there is a value in it
                    return True # this returns if the board is completely filled
                self.board[row][col] = 0 # this assigns a specified cell as an empty cell
        return False # this returns if the board is not completely filled

    def fill_values(self): # Constructs a solution to the current sudoku board
        self.fill_diagonal() # fills the three boxes along the main diagonal of the board
        self.fill_remaining(0, self.box_length) # fills the remaining cells in the board to create the solution

    def remove_cells(self): # Removes the appropriate number of cells from the board
        for i in range(self.removed_cells): # this iterates through every empty cell in the board
            row = random.randint(0, self.row_length - 1) # this randomly selects a row from 1-9
            col = random.randint(0, self.row_length - 1) # this randomly selects a column from 1-9
            while self.board[row][col] == 0: # this will always iterates for as long as a cell is empty
                row = random.randint(0, self.row_length - 1) # this randomly selects another row from 1-9
                col = random.randint(0, self.row_length - 1) # this randomly selects another column from 1-9
            self.board[row][col] = 0 # the randomly selected row and column with be designated as an empty space to be solved


def generate_sudoku(size, removed): # GIven the number of rows and number of cells to remove, this function creates a SudokuGenerator, fills its values, removes the appropriate number of cells, and returns the representative 2D lists of the board and solution
    sudoku = SudokuGenerator(size, removed) # this creates a sudoku generator board
    sudoku.fill_values() #this fills the board with random values
    key = str(sudoku.get_board()) # this returns an incomplete board
    print(key)
    sudoku.remove_cells() # this designates any empty cells to be 0
    board = sudoku.get_board() # this returns the solved version of the board
    return key, board
