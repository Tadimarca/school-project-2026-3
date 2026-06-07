import pygame
import math
import random
import time

pygame.init()
pygame.font.init()
pygame.mixer.init()

WIDTH = 800
HEIGHT = 600
FPS = 60
G = 1
T = 30

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (47, 23, 58)

font = pygame.font.SysFont("Arial", 36)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.display.set_caption("Tadimarca")

class Player:
    def __init__(self, image, x, y, width, height):
        self.speed = 400
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.transform.scale(pygame.image.load(f"images/{image}.png"), (width, height))
        self.image_rect = self.image.get_rect()
        self.old_rect = self.rect

    def draw(self):
        self.image_rect.x = self.rect.x
        self.image_rect.y = self.rect.y
        screen.blit(self.image, self.image_rect)

def spawn_walls():
    global walls
    n = 20
    walls = []
    for i in range(n):
        retry = True
        while retry:
            x = random.randint(0, WIDTH)
            y = random.randint(0, HEIGHT)
            width = random.randint(50, 100)
            height = random.randint(50, 100)
            rect = pygame.Rect(x, y, width, height)
            if not wolf.rect.colliderect(rect) and not fox.rect.colliderect(rect):
                retry = False
        walls.append(rect)

def draw():
    global first
    if game == 0:
        screen.fill(BLACK)
        for wall in walls:
            pygame.draw.rect(screen, PURPLE, wall)
        wolf.draw()
        fox.draw()
        text = font.render(str(T - t), True, WHITE)
        screen.blit(text, (0, 0))
    if game == 1:
        screen.fill(RED)
        image = pygame.transform.scale(pygame.image.load("images/lose.jpg"), (WIDTH, HEIGHT))
        image_rect = image.get_rect()
        screen.blit(image, image_rect)
        lose_sound.play()
    if game == 2:
        screen.fill(RED)
        image = pygame.transform.scale(pygame.image.load("images/win.jpg"), (WIDTH, HEIGHT))
        image_rect = image.get_rect()
        screen.blit(image, image_rect)
        if first:
            win_sound.play()
            first = False

def manage_keys1(key):
    return

def manage_keys2():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        wolf.rect.y -= wolf.speed * dt
    if keys[pygame.K_s]:
        wolf.rect.y += wolf.speed * dt
    if keys[pygame.K_a]:
        wolf.rect.x -= wolf.speed * dt
    if keys[pygame.K_d]:
        wolf.rect.x += wolf.speed * dt

    if wolf.rect.x > WIDTH:
        wolf.rect.x = 0
    if wolf.rect.x < 0:
        wolf.rect.x = WIDTH
    if wolf.rect.y > HEIGHT:
        wolf.rect.y = 0
    if wolf.rect.y < 0:
        wolf.rect.y = HEIGHT
    
    if keys[pygame.K_i]:
        fox.rect.y -= fox.speed * dt
    if keys[pygame.K_k]:
        fox.rect.y += fox.speed * dt
    if keys[pygame.K_j]:
        fox.rect.x -= fox.speed * dt
    if keys[pygame.K_l]:
        fox.rect.x += fox.speed * dt

    if fox.rect.x > WIDTH:
        fox.rect.x = 0
    if fox.rect.x < 0:
        fox.rect.x = WIDTH
    if fox.rect.y > HEIGHT:
        fox.rect.y = 0
    if fox.rect.y < 0:
        fox.rect.y = HEIGHT

def check_collision(rect1, rect2):
    global game
    if rect1.colliderect(rect2):
        game = 1
    for wall in walls:
        if fox.rect.colliderect(wall):
            fox.rect = fox.old_rect
        if wolf.rect.colliderect(wall):
            wolf.rect = wolf.old_rect

wolf = Player("wolf", random.randint(0, WIDTH), random.randint(0, HEIGHT), 30, 30)
fox = Player("fox", random.randint(0, WIDTH), random.randint(0, HEIGHT), 30, 30)

spawn_walls()

start = time.time()

first = True

win_sound = pygame.mixer.Sound("sounds/win_sound.wav")
lose_sound = pygame.mixer.Sound("sounds/lose_sound.wav")
pygame.mixer.music.load("sounds/music.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_pos(28.0)

game = 0
running = True
while running:
    dt = clock.tick(FPS) * 0.001
    t = time.time() - start

    if T - t < 0:
        game = 2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            manage_keys1(event.key)
    
    fox.old_rect = fox.rect.copy()
    wolf.old_rect = wolf.rect.copy()

    manage_keys2()
    check_collision(fox.rect, wolf.rect)
    draw()
    pygame.display.flip()

pygame.quit()