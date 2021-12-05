import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self,screen,ship,file_path):
        super().__init__()
        self.screen=screen
        self.image=pygame.image.load(file_path)
        self.mask=pygame.mask.from_surface(self.image)
        self.rect=self.image.get_rect()
        self.rect.centerx=ship.rect.centerx
        self.rect.bottom=ship.rect.top+40
        self.speed=5

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.y -= self.speed

