import pygame
import random

from Enemys import Enemy
from player import Player
pygame.init()
W = 1250 # width - ширина
H = 500 # height - высота

x = W // 2
y = H // 2

# FPS - Frames Per Second
fps = pygame.time.Clock()

# surface - поверхность
sc = pygame.display.set_mode((W, H))

img = pygame.image.load(r'C:\Users\morom\Downloads\circle.png')
#img = pygame.transform.rotate(img, 90)

#E1=Enemy(W, img, 20, 100, 0)

def draw():
    sc.fill((255, 255, 255))
    # pygame.draw.circle(sc, (25, 200, 200), (x, y), 100)
    E1._draw_(sc,H)
    #pygame.draw.circle(sc, (255, 200, 200), (0, H // 2), 100, 3)
    #pygame.draw.rect(sc, (0, 0, 0), (W // 2, H // 2, 100, 50), 2)
    pygame.display.update()
# главный цикл
while True:
    # проверка на нажатие крестика
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    
    # проверка на нажатие клавиш

    # отрисовка
    draw()

    # x += 1
    # y += 1
    # if x > W and y > H:
    #     x = 0
    #     y = 0

    # pygame.time.delay(10)
    fps.tick(120)


# (x, y) = (0, 3)
# print(x ,y)