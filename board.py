import pygame
from cell import Cell


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width - 4
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board = None  # Class variable for storing the board generated by the SudokuGenerator with spaces removed
        self.key = None  # Class variable for storing the board generated by the SudokuGenerator without spaces removed
        self.selected_cell = None  # Class variable for storing the currently selected cell
        self.current_answer = None  # Class variable for storing a board of integer values of all cells in self.board
        # Constructor for the Board class.
        # screen is a window from PyGame.
        # difficulty is a variable to indicate if the
        # user chose easy, medium, or hard

    def set_board(self, board):
        for row in board:
            for space in row:
                new_cell = Cell(
                    space,
                    board.index(row),
                    row.index(space),
                    self.screen,
                    space == 0
                )
                new_cell.set_board_dimensions(self.width, self.height)
                board[board.index(row)][row.index(space)] = new_cell
        self.board = board
        # Loops iterate through every space in the board and assign it with a Cell object,
        # the last parameter determining whether or not the space is originally blank and therefore editable.

    def set_key(self, key):
        self.key = key

    def draw(self):
        for row in self.board:  # Iterates through rows and cells of board and draws each cell
            for cell in row:
                cell.draw()
        for i in range(0, 4):
            pygame.draw.line(
                self.screen,
                (0, 0, 0),
                (0, i * (self.height/ 3)),
                (self.width + 8, i * (self.height/ 3)),
                8
            )
        for i in range(0, 4):
            pygame.draw.line(
                self.screen,
                (0, 0, 0),
                (i * (self.width / 3), 0),
                (i * (self.width / 3), self.height),
                8
            )
        # Last two for loops generate the bold border and 3x3 dividers iterating through thirds of the screen for
        # position.
        # Draws an outline of the Sudoku grid,
        # with bold lines to delineate the 3x3 boxes.
        # Draws every cell on this board.

    def select(self, row, col):
        if self.board[row][col].editable:  # Checks to see if the selected cell is editable in the first place
            if self.selected_cell is not None:
                self.selected_cell.selection(False)  # If a cell is already assigned as selected
            self.selected_cell = self.board[row][col]  # Sets the clicked on cell as the selected cell
            self.selected_cell.selection(True)  # Sets selection attribute of selected cell as True
            self.selected_cell.draw()
        # Marks the cell at (row, col)
        # in the board as the current selected cell.
        # Once a cell has been selected,
        # the user can edit its value or sketched value.

    def click(self, x, y):
        if x in range(0, self.width + 1) and y in range(0, self.height + 1):  # Checks that the click is within the board
            click_col = int(x // (self.width / 9))
            click_row = int(y // (self.height / 9))
            return click_row, click_col  # Returns the amount of rows down and amount of columns over that click is
        else:
            return None  # If click is outside the board then nothing is done to the board object.
        # If a tuple of (x, y) coordinates is within the displayed board,
        # this function returns a tuple of the (row, col) of the cell
        # which was clicked. Otherwise, this function returns None.

    def clear(self):
        self.selected_cell.set_cell_value(0)
        # Clears the value of the selected cell.
        # Note that the user can only remove the cell values and
        # sketched value that are filled by themselves.

    def sketch(self, value):
        self.selected_cell.set_sketched_value(value)
        # Sets the sketched value of the current selected cell equal
        # to user entered value. It will be displayed at the top left
        # corner of the cell using the draw() function.

    def place_number(self, value):
        self.selected_cell.set_cell_value(value)
        # Sets the value of the current selected cell equal to user
        # entered value. Called when the user presses the Enter key.

    def reset_to_original(self):  # Iterates through every cell in the board and sets the value to 0 of all editable cells
        for row in self.board:
            for cell in row:
                if cell.editable:
                    cell.set_cell_value(0)
        # Reset all cells in the board to their original values
        # (0 if cleared, otherwise the corresponding digit).

    def is_full(self): # Iterates through every cell in the board checking to see if any have a value of 0, meaning they are empty.
        is_full = True
        for row in self.board:
            for cell in row:
                if cell.value == 0:
                    is_full = False
        return is_full
        # Returns a Boolean value indicating whether the board is full
        # or not.

    def update_board(self):
        self.current_answer = str([[cell.value for cell in row] for row in self.board])
    # Sets the current answer equal to a new array of all VALUES of cells in the board.

    def find_empty(self):
        for row in self.board:
            for cell in row:
                if cell == 0:
                    return self.board.index(row), row.index(cell)
        # Finds an empty cell and returns its row and col as a
        # tuple of (x, y,).

    def check_board(self):
        self.update_board()
        if self.current_answer == self.key:
            return True
        else:
            return False
        # Checks whether the Sudoku board is solved correctly, aka whether the current answer matches the key.
