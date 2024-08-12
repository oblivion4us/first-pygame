import random
import pygame
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Тир")
icon = pygame.image.load("images/titleimg.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("images/targetimg1.png")
target_width = 50
target_height = 50

target_x = random.randint(0, SCREEN_WIDTH-target_width)
target_y = random.randint(0, SCREEN_HEIGHT-target_height)

color = (220,220,220)

score = 0
font = pygame.font.Font(None, 36)

hit_count = 0
last_hit_time = time.time()
double_score_bonus = False

running = True
while running:
    screen.fill(color)
    current_time = time.time()

    # Сброс счетчика попаданий если прошла секунда
    if current_time - last_hit_time >= 1:
        hit_count = 0
        double_score_bonus = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                hit_count += 1
                last_hit_time = current_time

                if hit_count > 5:
                    score += 2  # Удвоение очков
                    double_score_bonus = True
                else:
                    score += 1

    screen.blit(target_img, (target_x, target_y))

    score_text = font.render(f"Очки: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    if double_score_bonus:
        bonus_text = font.render("x2", True, (255, 0, 0))
        screen.blit(bonus_text, (10, 40))

    pygame.display.update()


pygame.quit()
