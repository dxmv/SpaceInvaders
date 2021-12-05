import pygame.sprite
from enemy import Alien
from random import randint
from game_functions import collide

ALIEN_WIDTH,ALIEN_HEIGHT=(40,32)
SPACE_BETWEEN=10

class EnemyGroup(pygame.sprite.Group):
    def __init__(self,WIDTH,screen):
        super().__init__()
        self.screen=screen
        self.WIDTH=WIDTH
        self.aliens=[]

    def create_aliens(self, num_of_aliens):
        for i in range(num_of_aliens):
            x,y=(randint(100,self.WIDTH-100),randint(-1500,-100))
            self.aliens.append(Alien(self.screen, x, y,randint(0,2)))

    def update(self, *args, **kwargs) -> None:
        for alien in self.aliens:
            alien.update()
            if alien.rect.bottom<=0:
                alien.kill()

    def draw(self):
        for alien in self.aliens:
            alien.draw()

    def check_collisions(self,bullets:pygame.sprite.Group,score:int):
        for alien in self.aliens:
            for bullet in bullets:
                if collide(alien,bullet):
                    bullet.kill()
                    self.aliens.remove(alien)
                    score[0]+=10

    def check_bottom(self,lives):
        for alien in self.aliens:
            if alien.rect.bottom>=800:
                lives[0]-=1
                self.aliens.remove(alien)

