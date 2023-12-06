import pygame


class Cell:
    def __init__(self, value, row, col, screen, editable, original):
        self.value = value  # Permanent value put in after the user hits enter on a sketched in cell
        self.row = row
        self.col = col
        self.screen = screen
        self.selected = False  # Whether the cell is currently selected or not
        self.sketched_value = None  # Temporary value input by the user
        self.editable = editable  # Whether the cell can be changed or not
        self.board_width = None
        self.board_height = None
        self.original = original  # Whether the cell is filled in or blank at the start
        # Constructor for the Cell class

    def selection(self, state):
        self.selected = state

    def set_board_dimensions(self, width, height):
        self.board_width = width
        self.board_height = height

    def set_cell_value(self, value):
        self.editable = False
        self.value = value
        # Setter for this cell's value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):  # Draws this cell, along with the value inside it.
        width = self.board_width - 4
        height = self.board_height
        # grabs the size of the screen the cell is to be printed on
        left = (width / 9) * self.col
        top = (height / 9) * self.row
        # right = (width / 9) * (self.col + 1)
        # bottom = (height / 9) * (self.row + 1)
        box_width = width / 9
        box_height = height / 9
        # based on the size of the screen, calculates the sides of the cell
        if self.selected:
            outline_color = (255, 0, 0)
        else:
            outline_color = (105, 105, 105)
        # changes outline color based on whether the cell has been selected
        pygame.draw.rect(
            self.screen,
            (255, 255, 255),
            (left, top, box_width, box_height)
        )
        pygame.draw.rect(
            self.screen,
            outline_color,
            (left, top, box_width, box_height),
            1
        )
        if self.sketched_value is not None:
            cell_number = pygame.font.SysFont("Arial", 20).render(str(self.sketched_value), True, (105, 105, 105))
            self.screen.blit(cell_number, (left + (box_width / 8), top + (box_height / 10)))
        if self.value != 0:
            # If this cell has a nonzero value, that value is displayed. # Otherwise, no value is displayed in the cell.
            num_color = (0, 0, 0)
            if self.original:
                num_color = (0, 0, 128)
            # If the cell is not empty at the start then the number color will be navy blue, otherwise it will be black
            cell_number = pygame.font.SysFont("Arial", 30).render(str(self.value), True, num_color)
            # Creates the number text object that will be displayed
            self.screen.blit(cell_number, (left + (box_width / 2) - 5, top + (box_height / 4)))
            # Actually displays said number
