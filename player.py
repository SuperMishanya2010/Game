import pygame

class Player:
    def __init__(self, x,y, size, img):
        self.x =x 
        self.y =y 
        self.size = size
        self.img = img

    def _draw_(self, sc, H):
        sc.blit(img (self.x,self.y ))

    def _move_right_(self):
            self.x += 1
    def _move_left_(self):
            self.x -= 1
    def _move_up_(self):
            self.y+=1
    def _move_down_(self):
            self.y-=1
    def rotate(self):
        self.img = pygame.transform.rotate(self.img, 2)
