import pygame
import random

pygame.init()
screen=pygame.display.set_mode((700,700))
pygame.display.set_caption("Good shot")

alien=pygame.transform.scale(pygame.image.load("alien.png"),(100,100))
bg=pygame.transform.scale(pygame.image.load("starry sky.png"),(700,700))
writing=pygame.font.SysFont("determination sans regular",50)
alienPos=pygame.Rect(300,300,100,100)

def draw():
    global hit,miss
    screen.blit(bg,(0,0))
    screen.blit(alien,(alienPos.x,alienPos.y))
    hit=writing.render("Hit!",True,"white")
    miss=writing.render("Miss",True,"white")

def click():
    global pos
    pos=pygame.mouse.get_pos()
    if pos==alienPos.collidepoint(alienPos.x,alienPos.y):
        alienPos.x=random.randint(100,600)
        alienPos.y=random.randint(100,600)
        screen.blit(hit,(20,50))
    elif pos!=alienPos.collidepoint(alienPos.x,alienPos.y):
        alienPos.x=random.randint(100,600)
        alienPos.y=random.randint(100,600) 
        screen.blit(miss,(20,50))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            click()
    draw()
    pygame.display.update()
