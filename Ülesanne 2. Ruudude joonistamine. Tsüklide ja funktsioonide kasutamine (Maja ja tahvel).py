import pygame
import sys
import random
pygame.init()
# värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
lGreen = [153, 255, 153]
# ekraani seaded
pind = pygame.display.set_mode([720, 550])
pygame.display.set_caption("Majake")
pind.fill(lGreen)
# funktsioonid
def drawHouse(x, y, width, height, screen, color):
    points = [(x, y - ((3 / 4.0) * height)), (x, y), (x + width, y), (x + width, y - (3 / 4.0) * height),
              (x, y - ((3 / 4.0) * height)), (x + width / 2.0, y - height), (x + width, y - (3 / 4.0) * height)]
    pygame.draw.lines(screen, color, False, points, 4)
#дверь
def drawDoor(x, y, width, height, screen, color):
    doorRect = pygame.Rect(x + (width - width / 4.0) / 2.0, y - height / 2.0, width / 4.0, height / 2.0)
    pygame.draw.rect(screen, color, doorRect, 4)
#окно
def drawWindow(x, y, width, height, screen, color):
    windowRect = pygame.Rect(x + width / 6.0, y - (3 / 5.0) * height, width / 5.0, width / 5.0)
    pygame.draw.rect(screen, color, windowRect, 4)
#дымоход
def drawChimney(x, y, width, height, screen, color):
    chimneyRect = pygame.Rect(x + (2 / 3.0) * width, y - height - (height / 4.0) / 2.0, width / 10.0, height / 4.0)
    pygame.draw.rect(screen, color, chimneyRect, 4)

# kutsun funktsioonid välja
drawHouse(100, 400, 300, 400, pind, red)
drawDoor(100, 400, 300, 400, pind, blue)
drawWindow(100, 400, 300, 400, pind, blue)
drawChimney(100, 400, 300, 400, pind, blue)

pygame.display.flip()
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
