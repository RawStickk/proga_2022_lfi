import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 1
screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

points = 0

def new_ball():
    '''
    draws a new ball
    '''
    global x, y, r
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def score(hit, points):
    '''
    hit - is the ball hit or not
    points - current score

    returns updated score if the ball is hit
    '''
    if (hit): points += 1
    print("Your score is", points)

    return points

def click(event):
    '''
    param: event - click on the screen
    prints whether you hit the ball
    '''
    global x, y, r
    hit = (x - event.pos[0]) ** 2 + (y - event.pos[1]) ** 2 <= r ** 2
    print(hit)
    return hit

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            points = score(click(event), points)
            print('Click!')
    for i in range(randint(1, 5)):
        new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()