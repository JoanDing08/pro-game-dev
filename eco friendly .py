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
  def update():
    pos=pygame.mouse.get_pos()

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

for i in range(40):
  item=recyclable(random.choice(recycle))
  item.rect.x=(random.randint(30,770))
  item.rect.y=(random.randint(30,670))
  allsprites.add(item)
  recyclables.add(item)

for i in range(10):
  trash=nonrecyclable()
  trash.rect.x=(random.randint(30,770))
  trash.rect.y=(random.randint(30,670))
  allsprites.add(trash)
  nonrecyclables.add(trash)

while True:
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      exit()
  allsprites.draw(screen)
  pygame.display.update()
