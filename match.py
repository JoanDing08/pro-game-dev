import pygame

pygame.init()

screen=pygame.display.set_mode((600,700))
screen.fill("black")

subwaySurfers=pygame.image.load("subway surfers.png")
ludo=pygame.image.load("ludo.png")
candyCrush=pygame.image.load("candycrush.jpg")
templeRun=pygame.image.load("temple run.png")
font=pygame.font.SysFont("calibri",30)

objective=font.render("Match the image to the name: ",True,"white")
sTxt=font.render("Subway Surfers",True,"white")
lTxt=font.render("Ludo",True,"white")
cTxt=font.render("Candy Crush",True,"white")
tTxt=font.render("Temple Run",True,"white")

screen.blit(subwaySurfers,(100,160))
screen.blit(ludo,(100,260))
screen.blit(candyCrush,(100,360))
screen.blit(templeRun,(100,460))
screen.blit(objective,(10,50))
screen.blit(sTxt,(300,260))
screen.blit(lTxt,(300,360))
screen.blit(cTxt,(300,460))
screen.blit(tTxt,(300,160))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            pos1=pygame.mouse.get_pos()
            circle1=pygame.draw.circle(screen,"grey",pos1,10,0)
            pygame.display.update()
        if event.type==pygame.MOUSEBUTTONUP:
            pos2=pygame.mouse.get_pos()
            circle2=pygame.draw.circle(screen,"grey",pos2,10,0)
            pygame.draw.line(screen,"grey",pos1,pos2,5)
            pygame.display.update()

    pygame.display.update()
