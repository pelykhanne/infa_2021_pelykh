import numpy as np
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
t = 0.45
screen = pygame.display.set_mode((int(2500 * t), int(1666 * t)))

yellow_sky_up = (254, 213, 162)
yellow_sky_middle = (254, 213, 148)
pink_sky = (254, 213, 196)
sun = (252, 238, 33)
orange_mountains = (252, 152, 49)
red_forest = (172, 67, 52)
pink_ground = (179, 134, 148)
dark_ground = (48, 16, 38)
dark_birds = (66, 33, 11)


def draw_backgroung():
    pygame.draw.rect(screen, yellow_sky_up, (0, 0, 2500 * t, 349 * t))
    pygame.draw.rect(screen, pink_sky, (0, 349 * t, 2500 * t, (841 - 349) * t))
    pygame.draw.rect(screen, yellow_sky_middle, (0, 711 * t, 2500 * t, (1065 - 711) * t))
    pygame.draw.rect(screen, pink_ground, (0, 1065 * t, 2500 * t, (2500 - 1666) * t))


def draw_sun():
    pygame.draw.circle(screen, sun, (1192 * t, 345 * t), (144 * t))


def draw_mountains():
    pygame.draw.polygon(screen, orange_mountains,
                        [[-30, 775 * t], [30 * t, 674 * t], [514 * t, 327 * t], [611 * t, 357 * t],
                        [644 * t, 411 * t], [653 * t, 419 * t], [958 * t, 625 * t],
                        [1123 * t, 603 * t], [1212 * t, 647 * t], [1331 * t, 531 * t], [1450 * t, 552 * t],
                        [1500 * t, 500 * t], [1770 * t, 265 * t], [1868 * t, 309 * t], [1980 * t, 415 * t],
                        [2071 * t, 390 * t], [2339 * t, 473 * t], [2325 * t, 471 * t],
                        [2500 * t, 755 * t]])
    for i in range(-1, 2):
        pygame.draw.arc(screen, orange_mountains, [1750 * t + i, 245 * t, 100 * t, 200 * t], 0, np.pi, int(200 * t))


def draw_forest():
    pygame.draw.polygon(screen, red_forest,
                        [[0, 1125 * t], [0, 830 * t], [71 * t, 858 * t], [250 * t, 825 * t],
                        [436 * t, 1068 * t], [546 * t, 885 * t], [723 * t, 979 * t],
                        [807 * t, 750 * t], [1000 * t, 800 * t], [1200 * t, 930 * t], [1430 * t, 876 * t],
                        [1750 * t, 687 * t], [2044 * t, 845 * t], [2153 * t, 755 * t], [2253 * t, 820 * t],
                        [2300 * t, 738 * t], [2407 * t, 743 * t], [2500 * t, 590 * t],
                        [2500 * t, 1071 * t]])
    for i in range(-1, 2):
        pygame.draw.arc(screen, red_forest, [1450 * t + i, 687 * t, 600 * t, 550 * t], np.pi / 2, np.pi * 0.9, int(200 * t))
    pygame.draw.arc(screen, red_forest, [60 * t + i, 660 * t, 400 * t, (900) * t], 0, np.pi * 5 / 6, int(383 * t))


def drawground():
    pygame.draw.polygon(screen, dark_ground,
                        [[0, 1666 * t], [0, 857 * t], [302 * t, 937 * t], [531 * t, 1232 * t],
                        [813 * t, 1580 * t], [1171 * t, 1637 * t], [1579 * t, 1408 * t],
                        [1689 * t, 1463 * t], [2089 * t, 1400 * t], [2500 * t, 1000 * t],
                        [2500 * t, 1666 * t]])


def print_bird(Xc, Yc, scale):
    dY = 50 * scale
    dX = 65 * scale
    r = 15 * scale
    pygame.draw.circle(screen, dark_birds, ((Xc - dX) * t, (Yc - dY) * t), (r * t))
    pygame.draw.polygon(screen, dark_birds,
                        [[(Xc - dX + r / 2 ** 0.5) * t - 1, (Yc - dY - r / 2 ** 0.5) * t],
                        [(Xc - dX - r / 2 ** 0.5) * t + 3, (Yc - dY + r / 2 ** 0.5) * t],
                        [Xc * t, Yc * t],
                        [(Xc + dX) * t, (Yc - dY) * t], [(Xc + dX / 2) * t, (Yc - dY * 2 / 2) * t],
                        [Xc * t, (Yc - dY / 2) * t]
                        ])

draw_backgroung()
draw_sun()
draw_mountains()
draw_forest()
drawground()

print_bird(960, 600, 1)
print_bird(1185, 621, 1)
print_bird(1185, 709, 1.05)
print_bird(991, 778, 1)
print_bird(1944, 1335, 1.5)
print_bird(1985, 1206, 0.6)
print_bird(1700, 1252, 0.8)
print_bird(1568, 1127, 1.0)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
