# main

import pygame
import numpy as np

WIDTH = 800
move_dist = 6 / 7
points = 10
circle = True
radius = 300
circle_detail = 30

if circle:
    focus_points = [[400 + radius * np.cos(2 * np.pi * k / circle_detail), 400 + radius * np.sin(2 * np.pi * k / circle_detail)] for k in range(circle_detail)]
else:
    focus_points = [[200, 200], [300, 0], [0, 0]]
dot = list(np.random.randint(0, 800, 2))

pygame.init()
w = pygame.display.set_mode((WIDTH, WIDTH))

def move():
    chosen = focus_points[np.random.randint(0, len(focus_points))]
    dot[0] += (chosen[0] - dot[0]) * move_dist
    dot[1] += (chosen[1] - dot[1]) * move_dist
    pygame.draw.circle(surface=w, color=(255, 255, 255), center=(dot[0], dot[1]), radius=2)

for point in focus_points:
    pygame.draw.circle(surface=w, color=(0, 255, 0), center=(point[0], point[1]), radius=5)

pygame.draw.circle(surface=w, color=(255, 255, 255), center=(dot[0], dot[1]), radius=2)

running = True
while running:
    # pygame.time.delay(10)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    move()
    for point in focus_points:
        pygame.draw.circle(surface=w, color=(0, 255, 0), center=(point[0], point[1]), radius=5)
    pygame.display.flip()