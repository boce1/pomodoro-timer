import pygame
import os
import sys
from visuals import display_time, running_display, waiting_display, display_circle
from config_ui import Config_window
from constants import *
import json

class Pg_window:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()

        self.font1 = pygame.font.SysFont("Consolas", HEIGHT // 10)
        self.icon = pygame.image.load("icon.ico")

        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pomodoro")
        pygame.display.set_icon(self.icon)

        self.study_seconds = 0
        self.rest_seconds = 0
        
        self.seconds_set = 0
        self.seconds_remaining = self.seconds_set 
        self.timer_stop = True
        self.alarm_path = None
        self.session = True # True for study session || False for pause session
        self.config_file = "config.json"

        self.character_index = 0
        self.characters = tuple(SPRITES.keys())

    def draw_scene(self, current_tick):
        circle_color = None
        if self.characters[self.character_index] == "sonic":
            circle_color = BLUE
        elif self.characters[self.character_index] == "shadow":
            circle_color = RED 

        self.window.fill(WHITE)
        display_circle(self.window, circle_color, WIDTH, HEIGHT, self.seconds_remaining, self.seconds_set)
        display_time(self.window, self.session, self.font1, BLACK, WIDTH, self.seconds_remaining)
        if self.timer_stop:
            waiting_display(self.window, current_tick, WIDTH, HEIGHT, SPRITES[self.characters[self.character_index]]["waiting"])
        else:
            running_display(self.window, current_tick, WIDTH, HEIGHT, SPRITES[self.characters[self.character_index]]["running"])
        pygame.display.update()

    def toogle_timer(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.timer_stop = not self.timer_stop
                pygame.mixer.music.stop()

    def restart_timer(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                self.timer_stop = True
                self.read_file()
                if self.session:
                    self.seconds_set = self.study_seconds
                else:
                    self.seconds_set = self.rest_seconds
                self.seconds_remaining = self.seconds_set
                pygame.mixer.music.stop()

    def switch_session(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.timer_stop = True
                self.session = not self.session
                if self.session:
                    self.seconds_set = self.study_seconds
                else:
                    self.seconds_set = self.rest_seconds
                self.seconds_remaining = self.seconds_set

    def change_character(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.character_index += 1

            if event.key == pygame.K_DOWN:
                self.character_index -= 1

            if self.character_index >= len(self.characters):
                self.character_index = 0
            if self.character_index < 0:
                self.character_index = len(self.characters) - 1

    def create_file(self):
        if not os.path.exists(self.config_file):
            dict_time = {
                "study_time" : 30 * 60, # default 30 minutes
                "rest_time" : 10 * 60, # default 10 minutes
                "alarm" : "./assets/alarms/alarm.wav" 
            }

            with open("config.json", "w") as outfile:
                json.dump(dict_time, outfile)

    def read_file(self):
        self.create_file()
        with open(self.config_file, "r") as file:
            content = file.read()
            data = json.loads(content)

            self.study_seconds = data["study_time"]
            self.rest_seconds = data["rest_time"]
            self.alarm_path = data["alarm"]

            self.seconds_set = self.study_seconds
            self.seconds_remaining = self.study_seconds # program starts with study sessions

            try:
                pygame.mixer.music.load(self.alarm_path)
            except pygame.error:
                self.alarm_path = None

    def edit_file(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.timer_stop = True
                self.session = True
                self.seconds_set = self.study_seconds
                self.seconds_remaining = self.seconds_set
                pygame.mixer.music.stop()

                self.create_file()
                Config_window().show()
                self.read_file()

    def play_alarm(self):
        if self.alarm_path:
            pygame.mixer.music.play(-1)

    def show(self):
        #self.create_file()
        self.read_file()
        run = True
        last_tick = pygame.time.get_ticks()

        clock = pygame.time.Clock()
        while run:
            clock.tick(FPS)
            current_tick = pygame.time.get_ticks()
            elapsed = (current_tick - last_tick) / 1000
            last_tick = current_tick
            if not self.timer_stop:
                self.seconds_remaining -= elapsed

            if self.seconds_remaining <= 0 and not self.timer_stop: # timer hasnt stopped yet, when idle
                self.play_alarm()

                self.session = not self.session
                self.timer_stop = True
                if self.session:
                    self.seconds_remaining = self.study_seconds
                    self.seconds_set = self.study_seconds
                else:
                    self.seconds_remaining = self.rest_seconds
                    self.seconds_set = self.rest_seconds

            self.draw_scene(current_tick)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                self.toogle_timer(event)
                self.restart_timer(event)
                self.switch_session(event)
                self.edit_file(event)
                self.change_character(event)

        pygame.quit()