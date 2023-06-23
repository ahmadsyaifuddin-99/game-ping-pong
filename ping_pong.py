import pygame
from pygame.locals import *

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
width = 640
height = 480

# Warna
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Inisialisasi layar
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

# Koordinat dan kecepatan pemain
player1_x = 20
player1_y = height // 2
player2_x = width - 20
player2_y = height // 2
player_speed = 5

# Inisialisasi skor
player1_score = 0
player2_score = 0
font = pygame.font.Font(None, 36)

# Bola
ball_x = width // 2
ball_y = height // 2
ball_speed_x = 3
ball_speed_y = 3
ball_radius = 10

# Fungsi untuk menggambar pemain
def draw_players():
    pygame.draw.rect(screen, WHITE, Rect((player1_x, player1_y - 50), (10, 100)))
    pygame.draw.rect(screen, WHITE, Rect((player2_x, player2_y - 50), (10, 100)))

# Fungsi untuk menggambar bola
def draw_ball():
    pygame.draw.circle(screen, WHITE, (ball_x, ball_y), ball_radius)

# Fungsi untuk menggambar skor
def draw_score():
    score_text = font.render(str(player1_score) + " - " + str(player2_score), True, WHITE)
    screen.blit(score_text, ((width // 2) - 40, 10))

# Loop utama permainan
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)  # Batasi kecepatan frame ke 60 FPS

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[K_w] and player1_y > 50:
        player1_y -= player_speed
    if keys[K_s] and player1_y < height - 50:
        player1_y += player_speed
    if keys[K_UP] and player2_y > 50:
        player2_y -= player_speed
    if keys[K_DOWN] and player2_y < height - 50:
        player2_y += player_speed

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_y > height - ball_radius or ball_y < ball_radius:
        ball_speed_y *= -1

    if ball_x > width - ball_radius:
        ball_speed_x *= -1
        player1_score += 1
    elif ball_x < ball_radius:
        ball_speed_x *= -1
        player2_score += 1

    if (player1_x + 10 >= ball_x - ball_radius and player1_y - 50 <= ball_y <= player1_y + 50) or \
            (player2_x - 10 <= ball_x + ball_radius and player2_y - 50 <= ball_y <= player2_y + 50):
        ball_speed_x *= -1

    screen.fill(BLACK)
    draw_players()
    draw_ball()
    draw_score()
    pygame.display.flip()

pygame.quit()
