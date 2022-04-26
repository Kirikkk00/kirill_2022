import pygame
from pygame.draw import *

pygame.init()
screen = pygame.display.set_mode((600, 600))
FPS = 60

rect(screen, (158, 158, 158), (0, 0, 600, 600))
circle(screen, (255, 255, 0), (300, 300), 200)
circle(screen, (0, 0, 0), (300, 300), 200, 4)
rect(screen, (0, 0, 0), (160, 380, 280, 40))
circle(screen, (255, 0, 0), (210, 215), 40)
circle(screen, (0, 0, 0), (210, 215), 40, 3)
circle(screen, (0, 0, 0), (210, 215), 10)
polygon(screen, (0, 0, 0),[(150, 120), (160, 100), (290, 210), (280, 220)])
circle(screen, (255, 0, 0), (375, 220), 50)
circle(screen, (0, 0, 0), (375, 220), 20)
circle(screen, (0, 0, 0), (375, 220), 50, 3)
polygon(screen, (0, 0, 0), [(290, 200), (420, 70), (430, 100), (310, 215)])

pygame.display.update()
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    clock.tick(FPS)
