import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))
screen.fill((128, 128, 128))

circle(screen, (255, 255, 0), (300, 300), 200)
rect(screen, (0, 0, 0), (200, 400, 200, 30))
circle(screen, (255, 0, 0), (220, 220), 40)
circle(screen, (255, 0, 0), (375, 220), 30)
circle(screen, (0, 0, 0), (220, 220), 20)
circle(screen, (0, 0, 0), (375, 220), 15)
polygon(screen, (0, 0, 0), [(100,125), (290, 170), (280,195), (90, 145), (100,125)])
polygon(screen, (0, 0, 0), [(500,135), (310, 180), (320,205), (510, 150), (500, 135)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

