import pygame, sys
from sudoku_generator import SudokuGenerator
from sudoku_generator import generate_sudoku
from cell import Cell
from board import Board


BG_COLOR = (0, 33, 165)
LINE_COLOR = (250, 70, 22)
diff = 0
def draw_game_start(screen):
    WIDTH, HEIGHT = 600, 800

    # title font
    start_title_font = pygame.font.SysFont(None, 80)
    sub_title_font = pygame.font.Font(None, 65)
    button_font = pygame.font.Font(None, 50)

    # Background
    screen.fill(BG_COLOR)


    # draw title
    title_surface = start_title_font.render('Welcome to Sudoku', 0, LINE_COLOR)
    title_box = title_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 180))
    screen.blit(title_surface, title_box)

    title_surface = sub_title_font.render("Select Game Mode:", 0, LINE_COLOR)
    title_box = title_surface.get_rect(
        center = (WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(title_surface, title_box)

    # initialize difficulty buttons
    easy_text = button_font.render("Easy", 0, (255, 255, 255))
    medium_text = button_font.render("Medium", 0, (255, 255, 255))
    hard_text = button_font.render("Hard", 0, (255, 255, 255))

    # initialize difficulty button background color and text
    easy_surface = pygame.Surface(((easy_text.get_size()[0]) + 20, easy_text.get_size()[1] + 20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text, (10, 10))
    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    medium_surface.fill(LINE_COLOR)
    medium_surface.blit(medium_text, (10, 10))
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_text, (10, 10))

    # initialize difficulty buttons' rectangles
    easy_rectangle = easy_surface.get_rect(
        center=(WIDTH // 2 - 200, HEIGHT // 2 + 100))
    medium_rectangle = medium_surface.get_rect(
        center=((WIDTH // 2), HEIGHT // 2 + 100))
    hard_rectangle = hard_surface.get_rect(
        center=((WIDTH // 2) + 200, HEIGHT // 2 + 100))

    # draw buttons
    screen.blit(easy_surface, easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    global diff
                    diff = 1
                    return
                elif medium_rectangle.collidepoint(event.pos):
                    diff = 2
                    return
                elif hard_rectangle.collidepoint(event.pos):
                    diff = 3
                    return
            pygame.display.update()

def draw_game_over(screen):
    WIDTH, HEIGHT = screen.get_size()
    # game over text
    game_over_font = pygame.font.Font(None, 60)
    screen.fill(BG_COLOR)
    game_over_surface = game_over_font.render("Game Over!", 0, LINE_COLOR)
    game_over_rect = game_over_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(game_over_surface, game_over_rect)
    # restart button
    restart_font = pygame.font.Font(None, 30)
    restart_text = restart_font.render("Restart", 0, (255, 255, 255))
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(LINE_COLOR)
    restart_surface.blit(restart_text, (10, 10))
    restart_rectangle = restart_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 150))
    screen.blit(restart_surface, restart_rectangle)


def draw_game_win(screen):
    WIDTH, HEIGHT = screen.get_size()
    # show game won screen
    game_win_font = pygame.font.Font(None, 60)
    screen.fill(BG_COLOR)
    game_win_surface = game_win_font.render("Game Won!", 0, LINE_COLOR)
    game_win_rect = game_win_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(game_win_surface, game_win_rect)
    # exit button
    exit_font = pygame.font.Font(None, 30)
    exit_text = exit_font.render("Exit", 0, (255, 255, 255))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10, 10))
    exit_rectangle = exit_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 150))
    screen.blit(exit_surface, exit_rectangle)

if __name__ == '__main__':
    game_over = False
    pygame.init()
    WIDTH, HEIGHT = 600, 800
    BOARD_WIDTH, BOARD_HEIGHT = 600, 600
    # set width/height of window, initialize screen
    screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))

    cell_size = WIDTH // 9

    pygame.display.set_caption("Welcome to Sudoku")

    # draw start screen
    draw_game_start(screen)

    screen.fill(BG_COLOR)

    # make board
    if diff == 1:
        board = Board(BOARD_WIDTH, BOARD_HEIGHT, screen, "easy")
        key, sudoku = generate_sudoku(9, 30)
        board.set_key(key)
        board.set_board(sudoku)
    elif diff == 2:
        board = Board(BOARD_WIDTH, BOARD_HEIGHT, screen, "medium")
        key, sudoku = generate_sudoku(9, 40)
        board.set_key(key)
        board.set_board(sudoku)
    elif diff == 3:
        board = Board(BOARD_WIDTH, BOARD_HEIGHT, screen, "hard")
        key, sudoku = generate_sudoku(9, 50)
        board.set_key(key)
        board.set_board(sudoku)
    # draw board
    board.draw()


    # reset, restart, exit buttons
    button_font = pygame.font.Font(None, 30)
    reset_text = button_font.render("RESET", 0, (255, 255, 255))
    restart_text = button_font.render("RESTART", 0, (255, 255, 255))
    exit_text = button_font.render("EXIT", 0, (255, 255, 255))

    reset_surface = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
    reset_surface.fill(LINE_COLOR)
    reset_surface.blit(reset_text, (10, 10))
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(LINE_COLOR)
    restart_surface.blit(restart_text, (10, 10))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(LINE_COLOR)
    exit_surface.blit(exit_text, (10, 10))

    # initialize difficulty buttons' rectangles
    reset_rectangle = reset_surface.get_rect(
        center=(WIDTH // 6, HEIGHT - 100))
    restart_rectangle = restart_surface.get_rect(
        center=((WIDTH // 3) + 20, HEIGHT - 100))
    exit_rectangle = exit_surface.get_rect(
        center=((WIDTH // 4 * 2) + 40, HEIGHT - 100))

    # draw buttons
    screen.blit(reset_surface, reset_rectangle)
    screen.blit(restart_surface, restart_rectangle)
    screen.blit(exit_surface, exit_rectangle)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # reset button clicked
                if reset_rectangle.collidepoint(event.pos):
                    board.reset_to_original()
                    board.draw()
                # restart button clicked
                elif restart_rectangle.collidepoint(event.pos):
                    draw_game_start(screen)
                    board.draw()
                # exit button clicked
                elif exit_rectangle.collidepoint(event.pos):
                    sys.exit()
                else:
                    # get mouse position
                    x, y = pygame.mouse.get_pos()
                    clicked_row, clicked_col = board.click(x, y)
                    board.select(clicked_row, clicked_col)
                    board.draw()
            if event.type == pygame.KEYDOWN:
                if event.key in range(49, 58) and board.selected_cell is not None:
                    board.selected_cell.set_sketched_value(event.key - 48)
                    board.draw()
                if event.key == 13 and board.selected_cell is not None:
                    if board.selected_cell.sketched_value is not None:
                        board.selected_cell.set_cell_value(board.selected_cell.sketched_value)
                        board.selected_cell.set_sketched_value(None)
                        board.draw()
            if board.is_full():
                if board.check_board():
                    draw_game_win(screen)
                else:
                    draw_game_over(screen)

        pygame.display.update()
