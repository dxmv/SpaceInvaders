import pygame

colors = ["D:\\Python projekti\\Space Invaders\\assets\\images\\pixel_ship_blue_small.png",
        "D:\\Python projekti\\Space Invaders\\assets\\images\\pixel_ship_red_small.png",
        "D:\\Python projekti\\Space Invaders\\assets\\images\\pixel_ship_green_small.png"
]

SPEED = 1


class Enemy(pygame.sprite.Sprite):

    def __init__(self,screen,x:int,y:int,file_path):
        super(Enemy, self).__init__()
        self.screen=screen
        self.image=pygame.image.load(file_path)
        self.mask=pygame.mask.from_surface(self.image)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.y +=SPEED


class Alien(Enemy):

    def __init__(self,screen,x:int,y:int,color:int):
        super().__init__(screen,x,y,colors[color])



