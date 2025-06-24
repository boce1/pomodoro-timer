import pygame
from math import pi, cos, sin
from constants import IMAGE_SIZE
import os

def count_sprites(directory):
    items = os.listdir(directory)
    files = [item for item in items if os.path.isfile(os.path.join(directory, item))]
    return len(files)

def display_time(win, session, font, color, width, seconds_remaining):
    if session:
        session_msg = font.render("Study sesion", True, color)
    else:
        session_msg = font.render("Rest", True, color)
    win.blit(session_msg, (width // 2 - session_msg.get_width() // 2, session_msg.get_height() // 2))
    
    seconds_remaining = round(seconds_remaining)
    hours = seconds_remaining // 3600
    minutes = (seconds_remaining - hours * 3600) // 60
    seconds = (seconds_remaining - hours * 3600 - minutes * 60)
    msg = font.render(f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}", True, color)
    win.blit(msg, (width // 2 - msg.get_width() // 2, session_msg.get_height() // 2 * 3 + msg.get_height() // 2))

def running_display(win, current_tick, width, height, path):
    index = int(current_tick / 60 % count_sprites(path))
    try:
        running_sonic = pygame.image.load(f"{path}//{index}_r.png")
        scaled_image = pygame.transform.scale(running_sonic, IMAGE_SIZE)
        win.blit(scaled_image, (width // 2 - scaled_image.get_width() // 2, height - 6/5 * scaled_image.get_height()))
    except pygame.error:
        print(f"Image {index}_r.png missing!")

def waiting_display(win, current_tick, width, height, path):
    index = int(current_tick / 60 % count_sprites(path))
    try:
        waiting_sonic = pygame.image.load(f"{path}//{index}_w.png")
        scaled_image = pygame.transform.scale(waiting_sonic, IMAGE_SIZE)
        win.blit(scaled_image, (width // 2 - scaled_image.get_width() // 2, height - 6/5 * scaled_image.get_height()))
    except pygame.error:
        print(f"Image {index}_w.png missing!")

def display_circle(win, color, background_color, width, height, seconds_remaining, seconds_set):
    padding = 10

    center_x = width // 2
    outer_radius = width // 4 - padding
    center_y = height - outer_radius - padding
    inner_radius = width // 4 - 2*padding
    
    start_angle = pi / 2
    end_angle = pi / 2 - (seconds_set - seconds_remaining) / seconds_set * 2 * pi

    pygame.draw.circle(win, color, (center_x, center_y), outer_radius)
    pygame.draw.circle(win, background_color, (center_x, center_y), inner_radius)

    if seconds_remaining != seconds_set:
        segments = (round(seconds_set - seconds_remaining) + 1) * 5
        points = [(center_x, center_y)]
        step = (start_angle - end_angle) / segments
        for i in range(segments + 1):
            angle = start_angle + i * step
            x = center_x - (outer_radius + padding) * cos(angle)
            y = center_y - (outer_radius + padding) * sin(angle)
            points.append((x, y))
        pygame.draw.polygon(win, background_color, points)