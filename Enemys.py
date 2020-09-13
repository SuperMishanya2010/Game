import pygame

class Enemy:
    def __init__(self, x, image, damage, size,revers):
        self.x =x 
        self.image = image
        self.damage = damage
        self.size = size

    def _draw_(self, sc, H):
        sc.blit(self.image (self.x,H-self.size ))

    def _move_(self):
            self.x -= 1
    def live(self):
        self._move_()
        self._draw_()
