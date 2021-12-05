import pygame
from game_functions import collide


class Player(pygame.sprite.Sprite):

    def __init__(self,screen):
        super().__init__()
        self.screen=screen
        self.image=pygame.image.load("D:\\Python projekti\\Space Invaders\\assets\\images\\player.png")
        self.mask=pygame.mask.from_surface(self.image)
        self.rect=self.image.get_rect()
        self.screenRect = self.screen.get_rect()
        self.rect.centerx = self.screenRect.centerx
        self.rect.bottom = self.screenRect.bottom-50
        self.right=False
        self.left=False
        self.up=False
        self.down=False
        self.speed=7

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.left and self.rect.left>=0:
            self.rect.x-=self.speed
        if self.right and self.rect.right<=1200:
            self.rect.x+=self.speed
        if self.up and self.rect.top>=0:
            self.rect.y-=self.speed
        if self.down and self.rect.bottom<=800:
            self.rect.y+=self.speed

    def check_collisions(self, aliens,lives):
        for alien in aliens.aliens:
            if collide(self,alien):
                lives[0]-=1
                aliens.aliens.remove(alien)