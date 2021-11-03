import pygame
import random
from pygame.locals import *


def on_grid_random():
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return (x//10 * 10, y//10 * 10)


def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake game')

snake = [(200, 200), (210, 200), (220, 200)]
my_direction = LEFT

snake_surface = pygame.Surface((10, 10))
snake_surface.fill((255, 255, 255))

apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))
apple_pos = on_grid_random()

clock = pygame.time.Clock()

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0, 0))

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)
    for pos in snake:
        screen.blit(snake_surface, pos)

    pygame.display.update()
