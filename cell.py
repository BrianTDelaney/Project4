import pygame


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.selected = False
        # Constructor for the Cell class

    def set_cell_value(self, value):
        self.value = value
        # Setter for this cell's value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):  # Draws this cell, along with the value inside it.
        width = self.screen.get_width()
        height = self.screen.get_height()
        # grabs the size of the screen the cell is to be printed on
        left = (width / 9) * self.col
        top = (height / 9) * self.row
        right = (width / 9) * (self.col + 1)
        bottom = (width / 9) * (self.row + 1)
        # based on the size of the screen, calculates the sides of the cell
        if self.selected:
            outline_color = (255, 0, 0)
        else:
            outline_color = (0, 0, 0)
        # changes outline color based on whether the cell has been selected
        pygame.draw.rect(
            self.screen,
            outline_color,
            (left, top, right, bottom),
            4
        )
        if self.value != 0:  # If this cell has a nonzero value, that value is displayed. # Otherwise, no value is displayed in the cell.
            cell_number = pygame.font.SysFont("Arial", 30).render(str(self.sketched_value), True, (0, 0, 0))  # Creates the number text object that will be displayed
            self.screen.blit(cell_number, ((left + right / 2), (top + bottom / 2)))  # Actually displays said number
