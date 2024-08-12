import random
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Тир")
icon = pygame.image.load("images/titleimg.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("images/targetimg.png")
target_width = 50
target_height = 50

target_x = random.randint(0, SCREEN_WIDTH-target_width)
target_y = random.randint(0, SCREEN_HEIGHT-target_height)

color = (220,220,220)

running = True
while running:
    pass

pygame.quit()
