import pygame
import math
import random

pygame.init()

f = 1
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Shooter")
icon = pygame.image.load('spaceship.png')
pygame.display.set_icon(icon)
ship_img = pygame.image.load('ufo.png')
player_chng = 0
no_of_enemies = 6

score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)


def print_score():
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (10, 10))


over_text = pygame.font.Font("freesansbold.ttf", 64)


def over():
    over = over_text.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over, (200, 250))


enemy_img = []
enemy_x = []
enemy_y = []
enemy_chngx = []
enemy_chngy = []

for i in range(no_of_enemies):
    enemy_img.append(pygame.image.load('monster.png'))
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(10, 100))
    enemy_chngx.append(2)
    enemy_chngy.append(40)

bulletIMG = pygame.image.load('bullet.png')
player_x = 370
player_y = 500

backg = pygame.image.load('background.png')

bulletX = 0
bulletY = 500
bullet_chngY = 10
bullet_state = "ready"

dis = 0


def iscollision(enemyx, enemyy, bulletx, bullety):
    dis = math.sqrt(math.pow(enemyx - bulletx, 2) + math.pow(enemyy - bullety, 2))
    if dis < 27:
        return True
    else:
        return False


def bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletIMG, (x + 16, y + 10))


def enemy(enemy_x, enemy_y, i):
    screen.blit(enemy_img[i], (enemy_x, enemy_y))


def player(player_x, player_y):
    screen.blit(ship_img, (player_x, player_y))


while f:

    screen.fill((0, 0, 0))
    screen.blit(backg, (0, 0))

    for i in range(no_of_enemies):

        if enemy_y[i] > 440:
            for j in range(no_of_enemies):
                enemy_y[j] = 1000
                over()
            break
        enemy_x[i] += enemy_chngx[i]
        if enemy_x[i] >= 736:
            enemy_x[i] = 736
            enemy_y[i] += enemy_chngy[i]
            enemy_chngx[i] *= -1
        elif enemy_x[i] <= 0:
            enemy_x[i] = 0
            enemy_y[i] += enemy_chngy[i]
            enemy_chngx[i] *= -1
        collision = iscollision(enemy_x[i], enemy_y[i], bulletX, bulletY)
        if collision:
            score_value += 1
            bullet_state = "ready"
            bulletY = 500
            enemy_y[i] = random.randint(10, 100)
            enemy_x[i] = random.randint(0, 736)
        enemy(enemy_x[i], enemy_y[i], i)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            f = 0
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                player_chng -= 5
            if i.key == pygame.K_RIGHT:
                player_chng += 5
            if i.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = player_x
                    bullet(bulletX, bulletY)
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_LEFT or i.key == pygame.K_RIGHT:
                player_chng = 0

    player_x += player_chng
    if player_x >= 736:
        player_x = 736
    elif player_x <= 0:
        player_x = 0

    if bulletY <= 0:
        bulletY = 500
        bullet_state = "ready"

    if bullet_state == "fire":
        bullet(bulletX, bulletY)
        bulletY -= bullet_chngY
    player(player_x, player_y)
    print_score()
    pygame.display.update()
