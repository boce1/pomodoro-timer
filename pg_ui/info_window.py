import pygame
from constants import *
from path import resource_path 

class Info_window:
    def __init__(self):
        self.x = WIDTH // 2 - INFO_WIDTH // 2
        self.y = HEIGHT // 2 - INFO_HEIGHT // 4

        left_arrow = pygame.image.load(resource_path(f"visuals/info/left_arrow.png"))
        self.left_arrow = pygame.transform.scale(left_arrow, (KEY_WIDTH, KEY_HEIGHT))

        right_arrow = pygame.image.load(resource_path(f"visuals/info/right_arrow.png"))
        self.right_arrow = pygame.transform.scale(right_arrow, (KEY_WIDTH, KEY_HEIGHT))

        up_arrow = pygame.image.load(resource_path(f"visuals/info/up_arrow.png"))
        self.up_arrow = pygame.transform.scale(up_arrow, (KEY_WIDTH, KEY_HEIGHT))

        down_arrow = pygame.image.load(resource_path(f"visuals/info/down_arrow.png"))
        self.down_arrow = pygame.transform.scale(down_arrow, (KEY_WIDTH, KEY_HEIGHT))

        i_key = pygame.image.load(resource_path(f"visuals/info/i_key.png"))
        self.i_key = pygame.transform.scale(i_key, (KEY_WIDTH, KEY_HEIGHT))

        esc_key = pygame.image.load(resource_path(f"visuals/info/esc_key.png"))
        self.esc_key = pygame.transform.scale(esc_key, (KEY_WIDTH, KEY_HEIGHT))

        space = pygame.image.load(resource_path(f"visuals/info/space.png"))
        self.space = pygame.transform.scale(space, (SPACE_KEY_WIDTH, KEY_HEIGHT))

        enter = pygame.image.load(resource_path(f"visuals/info/enter.png"))
        self.enter = pygame.transform.scale(enter, (ENTER_KEY_WIDTH, ENTER_KEY_HIGHT))

        pygame.font.init()
        font = pygame.font.SysFont("Consolas", INFO_HEIGHT // 15)
        self.first_row_msg = font.render("Change sessions", True, BLACK)
        self.second_row_msg = font.render("Change character", True, BLACK)
        self.third_row_msg = font.render("Open/close InfoWindow", True, BLACK)
        self.forth_row_msg = font.render("Open config window", True, BLACK)
        self.fifth_row_msg = font.render("Pause/resume", True, BLACK)
        self.sixth_row_msg = font.render("Restart timer", True, BLACK)

    def show(self, win):
        pygame.draw.rect(win, WHITE, (self.x, self.y, INFO_WIDTH, INFO_HEIGHT))
        pygame.draw.rect(win, BLACK, (self.x, self.y, INFO_WIDTH, INFO_HEIGHT), 1)

        # first row
        win.blit(self.left_arrow, (self.x + GAP, self.y + GAP))
        win.blit(self.right_arrow, (self.x + KEY_WIDTH + 2 * GAP, self.y + GAP))
        win.blit(self.first_row_msg, (self.x + 2*KEY_WIDTH + 3*GAP,
                                       self.y + GAP + KEY_HEIGHT//2 - self.first_row_msg.get_height() // 2))

        # second row
        win.blit(self.up_arrow, (self.x + GAP, self.y + GAP + KEY_HEIGHT + GAP))
        win.blit(self.down_arrow, (self.x + KEY_WIDTH + 2*GAP, self.y + KEY_HEIGHT + 2*GAP))
        win.blit(self.second_row_msg, (self.x + 2*KEY_WIDTH + 3*GAP,
                                        self.y + KEY_HEIGHT + 2*GAP + KEY_HEIGHT//2 - self.second_row_msg.get_height() // 2))

        # third row
        win.blit(self.i_key, (self.x + GAP, self.y+ 2*KEY_HEIGHT + 3*GAP))
        win.blit(self.third_row_msg, (self.x + KEY_WIDTH + 2*GAP,
                                       self.y+ 2*KEY_HEIGHT + 3*GAP + self.third_row_msg.get_height()//2))

        # forth row
        win.blit(self.esc_key, (self.x + GAP, self.y + 3*KEY_HEIGHT+ 4*GAP))
        win.blit(self.forth_row_msg, (self.x + KEY_WIDTH + 2*GAP,
                                       self.y + 3*KEY_HEIGHT+ 4*GAP + KEY_HEIGHT//2 - self.forth_row_msg.get_height()//2))

        # fifth row
        win.blit(self.space, (self.x + GAP, self.y + 4*KEY_HEIGHT+ 5*GAP))
        win.blit(self.fifth_row_msg, (self.x + SPACE_KEY_WIDTH + 2*GAP,
                                       self.y + 4*KEY_HEIGHT+ 5*GAP + KEY_HEIGHT//2 - self.fifth_row_msg.get_height()//2))

        # sixth row
        win.blit(self.enter, (self.x + GAP, self.y + 5*KEY_HEIGHT+ 6*GAP))
        win.blit(self.sixth_row_msg, (self.x + ENTER_KEY_WIDTH + 2*GAP,
                                       self.y + 5*KEY_HEIGHT+ 6*GAP + ENTER_KEY_HIGHT // 2 - self.sixth_row_msg.get_height()//2))
