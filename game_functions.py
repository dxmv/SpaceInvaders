import sys
import pygame
from bullet import Bullet

HIGH_SCORE_FILE="D:\\Python projekti\\Space Invaders\\highscore.txt"


def event_handler(screen,player,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            keydown_events(event,screen,player,bullets)
        if event.type==pygame.KEYUP:
            keyup_events(event,player)

def keydown_events(event,screen,player,bullets):
    if event.key==pygame.K_LEFT:
        player.left=True
    if event.key == pygame.K_RIGHT:
        player.right = True
    if event.key==pygame.K_UP:
        player.up=True
    if event.key==pygame.K_DOWN:
        player.down=True
    if event.key == pygame.K_SPACE:
        # bullet_sound=mixer.Sound("D:\\Python projekti\\Space Invaders\\assets\\sound\\shoot.wav")
        # bullet_sound.play()
        bullets.add(Bullet(screen,player,"D:\\Python projekti\\Space Invaders\\assets\\images\\bullet.png"))

def keyup_events(event,player):
    if event.key==pygame.K_LEFT:
        player.left=False
    if event.key == pygame.K_RIGHT:
        player.right = False
    if event.key==pygame.K_UP:
        player.up=False
    if event.key==pygame.K_DOWN:
        player.down=False

def update_screen(player,bullets,aliens,score,lives):
    player.update()
    for bullet in bullets:
        bullet.update()
        if bullet.rect.bottom<=0:
            bullet.kill()
    aliens.update()
    aliens.check_bottom(lives)
    aliens.check_collisions(bullets,score)
    player.check_collisions(aliens,lives)



def draw_on_screen(screen,player,bullets,aliens,bg,level_text,font,score,high_score_text,lives):
    screen.blit(bg,(0,0))
    player.draw()

    # Bullets
    for bullet in bullets:
        bullet.draw()

    aliens.draw()

    # Text render
    screen.blit(level_text,(0,0))

    # Score
    score_text = font.render(f"Score: {score[0]}", 1, (255,255,255))
    score_rect=score_text.get_rect()
    screen.blit(score_text, (1200-(score_rect.width),0))

    # Lives
    lives_text = font.render(f"Lives: {lives[0]}", 1, (255,255,255))
    lives_rect=lives_text.get_rect()
    screen.blit(lives_text, (1200-(lives_rect.width),score_rect.height))

    # High score
    screen.blit(high_score_text,(0,score_rect.height))
    pygame.display.flip()

def collide(obj1,obj2):
    offset_x=obj2.rect.x-obj1.rect.x
    offset_y=obj2.rect.y-obj1.rect.y
    return obj1.mask.overlap(obj2.mask,(offset_x,offset_y)) != None

def get_high_score()->int:
    try:
        file=open(HIGH_SCORE_FILE)
        line=file.readlines()[0]
        return line
    except:
        return 0
    finally:
        file.close()

def set_high_score(score:int):
    file=open(HIGH_SCORE_FILE,"w")
    file.write(str(score[0]))
    file.close()