import pygame
import game_functions
from player import Player
from game_functions import event_handler,update_screen,draw_on_screen
from pygame.sprite import Group
from enemy_group import EnemyGroup

# Constants
SIZE=(1200, 800)

# Colors
BLACK=(0,0,0)
WHITE=(255,255,255)

pygame.init()

# Opens a new window
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Space invaders")
bg = pygame.image.load("D:\\Python projekti\\Space Invaders\\assets\\images\\background.jpg")


# Game variables
player=Player(screen)
bullets=Group()
aliens=EnemyGroup(1200,screen)
num_of_aliens=5
highscore=game_functions.get_high_score()
score=[0]
level=0
lives=[3]

# Main loop
carryOn = True
clock = pygame.time.Clock()

# Text
pygame.font.init()
font = pygame.font.SysFont("Arial", 35)
level_text=font.render(f"Level: {level}",1,WHITE)
high_score_text=font.render(f"High Score:{highscore}",1,WHITE)

while carryOn:
    event_handler(screen,player,bullets)
    draw_on_screen(screen,player,bullets,aliens,bg,level_text,font,score,high_score_text,lives)
    update_screen(player,bullets,aliens,score,lives)

    # All enemies destroyed
    if aliens.aliens.__len__() == 0:
        num_of_aliens += 2
        level += 1
        level_text = font.render(f"Level:{level}", 1, WHITE)
        aliens.create_aliens(num_of_aliens)

    # Check lives
    if lives[0] <= 0:
        carryOn = False

    clock.tick(60)
pygame.quit()

if score[0] > int(highscore):
    game_functions.set_high_score(score)
