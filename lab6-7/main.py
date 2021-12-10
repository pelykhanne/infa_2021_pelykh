from random import randint, random, choice
from math import pi, sin, cos, hypot

import pygame

FPS = 60

dt = 1 / FPS

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

MIN_VELOCITY, MAX_VELOCITY = 50, 200
MIN_RADIUS, MAX_RADIUS = 20, 50

N = 10


def gen_ball():
    v = randint(MIN_VELOCITY, MAX_VELOCITY)
    phi = random() * 2 * pi
    return {
        'x': randint(10, WIDTH - 10),
        'y': randint(10, HEIGHT - 10),
        'vx': v * cos(phi),
        'vy': v * sin(phi),
        'r': randint(MIN_RADIUS, MAX_RADIUS),
        'color': choice(GAME_COLORS)
    }


def draw():
    for ball in balls:
        pygame.draw.circle(screen, ball['color'], (ball['x'], ball['y']), ball['r'])


def move():
    for ball in balls:
        ball['x'] += ball['vx'] * dt
        ball['y'] += ball['vy'] * dt

        if ball['x'] < ball['r']:
            ball['vx'] = abs(ball['vx'])
        elif ball['x'] > WIDTH - ball['r']:
            ball['vx'] = -abs(ball['vx'])

        if ball['y'] < ball['r']:
            ball['vy'] = abs(ball['vy'])
        elif ball['y'] > HEIGHT - ball['r']:
            ball['vy'] = -abs(ball['vy'])


def process_click(pos):
    global score
    for ball in balls:
        if hypot(ball['x'] - pos[0], ball['y'] - pos[1]) <= ball['r']:
            balls.remove(ball)
            balls.append(gen_ball())
            score += 10


def draw_score(score):
    surface = font.render("Your score: " + str(score), False, BLACK)
    screen.blit(surface, (0, 0))


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font = pygame.font.Font(pygame.font.get_default_font(), 20)

score = 0
balls = []
for _ in range(N):
    balls.append(gen_ball())

finished = False

while not finished:
    clock.tick(FPS)
    screen.fill(WHITE)
    draw()
    draw_score(score)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            process_click(event.pos)

    move()
    pygame.display.update()
pygame.quit()
