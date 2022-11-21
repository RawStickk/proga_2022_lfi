import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 60
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
balls = []

def new_ball(balls):
    '''
    adds a new ball to the list
    balls - list of balls
    '''
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    Vx = randint(100, 200)
    Vy = randint(100, 200)
    color = COLORS[randint(0, 5)]
    balls.append([x, y, r, Vx, Vy, color])
    draw_ball([x, y, r, Vx, Vy, color])

def draw_ball(ball):
    '''
    draws a ball
    :param ball: parameters of a ball
    '''
    circle(screen, ball[5], (ball[0], ball[1]), ball[2])

def move(balls, dt):
    '''
    models movemt and reflection of the balls
    :param balls: list of properties of the balls
    :param dt: time interval
    '''
    for i in range(len(balls)):
        balls[i][0] += balls[i][3] * dt
        balls[i][1] += balls[i][4] * dt
        if (balls[i][0] - balls[i][2] < 0):
            balls[i][0] = balls[i][2]
            balls[i][3] *= -1
        if (balls[i][0] + balls[i][2] > 1200):
            balls[i][0] = 1200 - balls[i][2]
            balls[i][3] *= -1
        if (balls[i][1] - balls[i][2] < 0):
            balls[i][1] = balls[i][2]
            balls[i][4] *= -1
        if (balls[i][1] + balls[i][2] > 900):
            balls[i][1] = 900 - balls[i][2]
            balls[i][4] *= -1

        draw_ball(balls[i])

def score(hit, points):
    '''
    hit - is the ball hit or not
    points - current score

    returns updated score if the ball is hit
    '''
    if (hit): points += 1
    else: points -= 1

    return points

def click(event, balls):
    '''
    param: event - click on the screen
           balls - list of balls
    prints whether you hit the ball
    '''
    hit = False
    for i in range(len(balls)):
        hit = (balls[i][0] - event.pos[0]) ** 2 + (balls[i][1] - event.pos[1]) ** 2 <= balls[i][2] ** 2
        if (hit):
            balls.pop(i)
            break
    return hit

pygame.display.update()
clock = pygame.time.Clock()
finished = False

for i in range(randint(10, 20)):
    new_ball(balls)

score(0, 0)

font = pygame.font.Font('font_balls.ttf', 32)

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            points = score(click(event, balls), points)


    move(balls, 0.05)
    text = font.render(f"Your score is {points}", True, "#ffffff")
    screen.blit(text, (10, 10))

    pygame.display.update()
    screen.fill(BLACK)
    if(not balls):
        text1 = font.render("Game over", True, "#ffffff")
        screen.blit(text1, (500, 400))

pygame.quit()