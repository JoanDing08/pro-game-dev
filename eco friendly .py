import pygame
import random
import time
pygame.init()

pygame.display.set_caption("Eco-Friendly")
screen=pygame.display.set_mode((800,700))

class bin(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image=pygame.transform.scale(pygame.image.load("bin.png"),(50,50))
    self.rect=self.image.get_rect()

class recyclable(pygame.sprite.Sprite):
  def __init__(self,img):
    self.image=pygame.transform.scale(pygame.image.load(img),(50,50))
    self.rect=self.image.get_rect()

class nonrecyclable(pygame.sprite.Sprite):
  def __init__(self):
    self.image=pygame.transform.scale(pygame.image.load("bag.png"),(50,50))
    self.rect=self.image.get_rect()

allsprites=pygame.sprite.Group()
recyclables=pygame.sprite.Group()
nonrecyclables=pygame.sprite.Group()

player=bin()
allsprites.add(player)

recycle=["paper bag.png","pencil","crate.png"]

for i in range(50):
  item=recyclable(random.choice(recycle))
  item.rect.x=(random.randint(50,650))
  item.rect.y=(random.randint(50,650))
  allsprites.add(item)
  recyclables.add(item)



while True:
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      exit()
  allsprites.draw(screen)
  pygame.display.update()
