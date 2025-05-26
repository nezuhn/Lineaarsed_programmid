# import pygame, sys
# pygame.init()
# #värvid
# red = [255, 0, 0]
# green = [0, 255, 0]
# blue = [0, 0, 255]
# pink = [255, 153, 255]
# lGreen = [153, 255, 153]
# lBlue= [153, 204, 255]
# #ekraani seaded
# screenX = 640
# screenY = 240
# screen=pygame.display.set_mode([screenX,screenY])
# pygame.display.set_caption("Animeerimine_2")
# screen.fill(blue)
# clock = pygame.time.Clock()
# ball = pygame.image.load("Pall.png")#graafika laadimine
# #kiirus ja asukoht
# posX, posY = 0, 0
# speedX, speedY = 3,4
# gameover = False
# while not gameover:
#     clock.tick(60)
#     #mängu sulgemine ristist
#     events = pygame.event.get()
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             sys.exit()
#     #pildi liisamine ekraanile
#     screen.blit(ball, (posX, posY))
#     posX += speedX
#     posY += speedY
#     #kui puudub ääri, siis muudab suunda
#     if posX > screenX-ball.get_rect().width or posX < 0:
#         speedX = -speedX

#     if posY > screenY-ball.get_rect().height or posY <0:
#         speedY = -speedY
#         pygame.display.flip()
#         screen.fill(lBlue)
# pygame.quit()


import pygame, sys, random
pygame.init()
#värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
lBlue= [153, 204, 255]
#ekraani seaded
screenX = 640
screenY = 240
screen=pygame.display.set_mode([screenX,screenY])
pygame.display.set_caption("Animeerimine_2")
screen.fill(blue)
clock = pygame.time.Clock()
posX, posY = 0, 0
speedX, speedY = 3, 3
coords = [] #koordinaatide loomine ja lisamine massiivi
for i in range (10):
    posX = random.randint(1, screenX)
    posY = random.randint(1, screenY)
    coords.append([posX, posY])
gameover = False
while not gameover:
    clock.tick(120)
    events = pygame.event.get()#mängu sulgumine ristist
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    #loendist koordinaadid
    for i in range(len(coords)):
        pygame.draw.rect(screen,red, [coords[i][0], coords[i][1], 20,20])
        coords[i][1] +=1
        if coords[i][1] > screenY:#kui jõuab alla, siis muudame ruduu alguspunkti # 2
            coords[i][1] = random.randint(-40, -10)
            coords[i][0] = random.randint(0,screenX)
    pygame.display.flip()
    screen.fill(lBlue)
pygame.quit