import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping-Pong Pygame")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
paddle_speed = 7

BALL_SIZE = 20
ball_speed_x = 5
ball_speed_y = 5

paddle1 = pygame.Rect(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WIDTH - 20, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH//2 - BALL_SIZE//2, HEIGHT//2 - BALL_SIZE//2, BALL_SIZE, BALL_SIZE)

score1 = 0
score2 = 0
font = pygame.font.SysFont(None, 50)
end_font = pygame.font.SysFont(None, 100)

clock = pygame.time.Clock()

game_over = False

def draw():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    score_text = font.render(f"{score1} : {score2}", True, WHITE)
    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 20))

def draw_game_over():
    screen.fill(BLACK)
    end_text = end_font.render("THE END", True, WHITE)
    screen.blit(end_text, (WIDTH//2 - end_text.get_width()//2, HEIGHT//2 - end_text.get_height()//2))
    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not game_over:
        keys = pygame.key.get_pressed()
        # Управление первой ракеткой (W и S)
        if keys[pygame.K_w] and paddle1.top > 0:
            paddle1.y -= paddle_speed
        if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
            paddle1.y += paddle_speed

        # Управление второй ракеткой (стрелки вверх и вниз)
        if keys[pygame.K_UP] and paddle2.top > 0:
            paddle2.y -= paddle_speed
        if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
            paddle2.y += paddle_speed

        # Движение мяча
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Отскок мяча от верхнего и нижнего края
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y *= -1

        # Отскок мяча от ракеток
        if ball.colliderect(paddle1) and ball_speed_x < 0:
            ball_speed_x *= -1
        if ball.colliderect(paddle2) and ball_speed_x > 0:
            ball_speed_x *= -1

        # Голы и сброс мяча
        if ball.left <= 0:
            score2 += 1
            ball.center = (WIDTH//2, HEIGHT//2)
            ball_speed_x *= -1
        if ball.right >= WIDTH:
            score1 += 1
            ball.center = (WIDTH//2, HEIGHT//2)
            ball_speed_x *= -1

        # Проверка окончания игры
        if score1 >= 20 or score2 >= 20:
            game_over = True

        draw()
        pygame.display.flip()
    else:
        draw_game_over()

    clock.tick(60)
