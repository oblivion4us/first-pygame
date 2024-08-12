import random
import pygame
import time
import sys

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

color = (220, 220, 220)

score = 0
font = pygame.font.Font(None, 36)

hit_count = 0
last_hit_time = time.time()
double_score_bonus = False

game_duration = 30
scores = []

def get_nickname():
    """Функция для ввода никнейма."""
    nickname = ''
    input_active = True
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    nickname = nickname[:-1]
                else:
                    nickname += event.unicode
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))
        text_surface = font.render(f'Введите ваш никнейм: {nickname}', True, (0, 0, 0))
        screen.blit(text_surface, (50, SCREEN_HEIGHT / 3))
        pygame.display.flip()
    return nickname

def show_scoreboard(scores):
    """Функция для отображения таблицы лидеров."""
    screen.fill((255, 255, 255))
    scores.sort(key=lambda x: x[1], reverse=True)  # Сортировка по убыванию очков
    for i, (nickname, score) in enumerate(scores):
        text_surface = font.render(f'{i + 1}. {nickname}: {score}', True, (0, 0, 0))
        screen.blit(text_surface, (50, 50 + i * 30))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def main_game():
    global score, hit_count, double_score_bonus, last_hit_time
    score = 0
    hit_count = 0
    double_score_bonus = False
    last_hit_time = time.time()

    target_x = random.randint(0, SCREEN_WIDTH - target_width)
    target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    start_time = time.time()
    running = True
    while running:
        screen.fill(color)
        current_time = time.time()

        elapsed_time = current_time - start_time
        remaining_time = max(0, game_duration - elapsed_time)

        if elapsed_time > game_duration:
            nickname = get_nickname()
            scores.append((nickname, score))
            show_scoreboard(scores)
            running = False
            continue

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
                        score += 2
                        double_score_bonus = True
                    else:
                        score += 1

        screen.blit(target_img, (target_x, target_y))

        score_text = font.render(f"Очки: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        timer_text = font.render(f"Время: {int(remaining_time)}", True, (0, 0, 0))
        timer_rect = timer_text.get_rect(center=(SCREEN_WIDTH / 2, 20))
        screen.blit(timer_text, timer_rect)

        if double_score_bonus:
            bonus_text = font.render("x2", True, (255, 0, 0))
            screen.blit(bonus_text, (10, 40))

        pygame.display.update()

def start_screen():
    button_font = pygame.font.Font(None, 74)
    button_text = button_font.render("Начать", True, (0, 0, 0))
    button_rect = button_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

    running = True
    while running:
        screen.fill((220, 220, 220))  # Цвет фона серый (220, 220, 220)
        pygame.draw.rect(screen, (128, 0, 0), button_rect.inflate(20, 20))
        screen.blit(button_text, button_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    running = False

        pygame.display.flip()

start_screen()
main_game()

pygame.quit()