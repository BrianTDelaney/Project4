import pygame


class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        # Constructor for the Board class.
        # screen is a window from PyGame.
        # difficulty is a variable to indicate if the
        # user chose easy, medium, or hard

    def draw(self):
        for i in range(0, 4):
            pygame.draw.line(
                self.screen,
                (0, 0, 0),
                (0, i * (self.height / 3)),
                (self.width, i * (self.height / 3)),
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
        # Still have to set it up so it draws every cell
        pass
        # Draws an outline of the Sudoku grid,
        # with bold lines to delineate the 3x3 boxes.
        # Draws every cell on this board.

    def select(self, row, col):
        pass
        # Marks the cell at (row, col)
        # in the board as the current selected cell.
        # Once a cell has been selected,
        # the user can edit its value or sketched value.

    def click(self, x, y):
        if x in range(0, self.width + 1) and y in range(0, self.height + 1):
            pass
        else:
            return None
        pass
        # If a tuple of (x, y) coordinates is within the displayed board,
        # this function returns a tuple of the (row, col) of the cell
        # which was clicked. Otherwise, this function returns None.

    def clear(self):
        pass
        # Clears the value cell.
        # Note that the user can only remove the cell values and
        # sketched value that are filled by themselves.

    def sketch(self, value):
        pass
        # Sets the sketched value of the current selected cell equal
        # to user entered value. It will be displayed at the top left
        # corner of the cell using the draw() function.

    def place_number(self, value):
        pass
        # Sets the value of the current selected cell equal to user
        # entered value. Called when the user presses the Enter key.

    def reset_to_original(self):
        pass
        # Reset all cells in the board to their original values
        # (0 if cleared, otherwise the corresponding digit).

    def is_full(self):
        pass
        # Returns a Boolean value indicating whether the board is full
        # or not.

    def update_board(self):
        pass
        # Updates the underlying 2D board with the values in all cells.

    def find_empty(self):
        pass
        # Finds an empty cell and returns its row and col as a
        # tuple of (x, y,).

    def check_board(self):
        pass
        # Checks whether the Sudoku board is solved correctly.
