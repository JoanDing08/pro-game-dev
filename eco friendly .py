import pygame
import random
import time
pygame.init()

pygame.display.set_caption("Eco-Friendly")
screen=pygame.display.set_mode((800,700))
bg=pygame.transform.scale(pygame.image.load("eco friendly bg.png"),(800,700))
startTime=time.time()
score=0
minScore=10

font=pygame.font.SysFont("Calibri",40)
scoreTxt=font.render("Score: "+str(score),True,"white")

class bin(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image=pygame.transform.scale(pygame.image.load("bin.png"),(50,50))
    self.rect=self.image.get_rect()


class recyclable(pygame.sprite.Sprite):
  def __init__(self,img):
    pygame.sprite.Sprite.__init__(self)
    self.image=pygame.transform.scale(pygame.image.load(img),(50,50))
    self.rect=self.image.get_rect()

class nonrecyclable(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.image=pygame.transform.scale(pygame.image.load("bag.png"),(50,50))
    self.rect=self.image.get_rect()

allsprites=pygame.sprite.Group()
recyclables=pygame.sprite.Group()
nonrecyclables=pygame.sprite.Group()

player=bin()
allsprites.add(player)

recycle=["paper bag.png","pencil.png","crate.png"]

for i in range(20):
  item=recyclable(random.choice(recycle))
  item.rect.x=(random.randint(30,750))
  item.rect.y=(random.randint(30,650))
  allsprites.add(item)
  recyclables.add(item)

for i in range(5):
  trash=nonrecyclable()
  trash.rect.x=(random.randint(30,750))
  trash.rect.y=(random.randint(30,650))
  allsprites.add(trash)
  nonrecyclables.add(trash)

while True:
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      exit()
    
  timeElapsed=time.time()-startTime
  countDown=font.render(str(timeElapsed),True,"white")

  if timeElapsed>=25:
    if score>=minScore:
      screen.fill("green")
      success=font.render(f"Time's up. You got {score}/20. Great job.",True,"white")
      screen.blit(success,(10,350))
    else:
      screen.fill("red")
      fail=font.render(f"Time's up. You got {score}/20. Better luck next time.",True,"white")
      screen.blit(fail,(10,350))
  else:
    screen.blit(bg,(0,0))
    key=pygame.key.get_pressed()
    if key[pygame.K_UP] and player.rect.y>0:
      player.rect.y-=6
    if key[pygame.K_DOWN] and player.rect.y<800:
      player.rect.y+=6
    if key[pygame.K_LEFT] and player.rect.x>0:
      player.rect.x-=6
    if key[pygame.K_RIGHT] and player.rect.x<700:
      player.rect.x+=6
    
    r_list=pygame.sprite.spritecollide(player,recyclables,True)
    nr_list=pygame.sprite.spritecollide(player,nonrecyclables,True)
    for i in r_list:
      score+=1
      scoreTxt=font.render("Score: "+str(score),True,"white")
    for i in nr_list:
      score-=2
      scoreTxt=font.render("Score: "+str(score),True,"white")
    screen.blit(scoreTxt,(10,10))
    screen.blit(countDown,(770,670))

    allsprites.draw(screen)
  pygame.display.update()
