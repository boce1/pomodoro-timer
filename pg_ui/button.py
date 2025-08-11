import pygame as pg
from constants import *
from path import resource_path 

class Button:
    def __init__(self, x, y, width, height, shortcut, border_color = BLACK, color = WHITE):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.shortcut = shortcut
        self.border_color = border_color
        self.color = color
        self.actual_color = color

        info_icon = pg.image.load(resource_path(f".\\visuals\\info\\info.png"))
        self.info_icon = pg.transform.scale(info_icon, (self.width, self.height))

        x_icon = pg.image.load(resource_path(f".\\visuals\\info\\x.png"))
        self.x_icon = pg.transform.scale(x_icon, (self.width, self.height))

    def draw(self, win, cond=False):
        pg.draw.rect(win, self.actual_color, (self.x, self.y, self.width, self.height))
        pg.draw.rect(win, self.border_color, (self.x, self.y, self.width, self.height), 1)

        if cond:
            win.blit(self.x_icon, (self.x, self.y))
        else:
            win.blit(self.info_icon, (self.x, self.y))


    def is_mouse_in(self, mouse_pos):
        if(self.x <= mouse_pos[0] <= self.x + self.width and
           self.y <= mouse_pos[1] <= self.y + self.height):
            return True
        return False

    def is_mouse_pressed(self, mouse_pressed): # for coloring
        if mouse_pressed[0]:
            return True
        return False
    
    def is_pressed(self, mouse_pos, mouse_pressed):
        if self.is_mouse_in(mouse_pos) and self.is_mouse_pressed(mouse_pressed):
            self.actual_color = GRAY
        else:
            self.actual_color = self.color

    def is_clicked(self, event, mouse_pos): # for event handling
        if self.is_mouse_in(mouse_pos):
            if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                return True
        return False
    
    def is_shorcut_pressed(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == self.shortcut:
                return True
        return False