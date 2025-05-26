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
yellow = [255, 255, 0]
# ekraani seaded
pind = pygame.display.set_mode([720, 550])
pygame.display.set_caption("Majake")
pind.fill(lGreen)
# funktsioonid
def drawHouse(x, y, width, height, screen, color):
    points = [(x, y - ((3 / 4.0) * height)), (x, y), (x + width, y), (x + width, y - (3 / 4.0) * height),
              (x, y - ((3 / 4.0) * height)), (x + width / 2.0, y - height), (x + width, y - (3 / 4.0) * height)]
    pygame.draw.lines(screen, color, False, points, 4)

def drawDoor(x, y, width, height, screen, color):
    doorRect = pygame.Rect(x + (width - width / 4.0) / 2.0, y - height / 2.0, width / 4.0, height / 2.0)
    pygame.draw.rect(screen, color, doorRect, 4)

def drawWindow(x, y, width, height, screen, color):
    windowRect = pygame.Rect(x + width / 6.0, y - (3 / 5.0) * height, width / 5.0, width / 5.0)
    pygame.draw.rect(screen, color, windowRect, 4)

def drawChimney(x, y, width, height, screen, color):
    chimneyRect = pygame.Rect(x + (2 / 3.0) * width, y - height - (height / 4.0) / 2.0, width / 10.0, height / 4.0)
    pygame.draw.rect(screen, color, chimneyRect, 4)

def drawSun(screen, x, y, radius, color):
    pygame.draw.circle(screen, color, (x, y), radius, 4)
    for i in range(12):
        angle = i * (360 / 12)
        dx = radius * 1.5 * pygame.math.Vector2(1, 0).rotate(angle).x
        dy = radius * 1.5 * pygame.math.Vector2(1, 0).rotate(angle).y
        pygame.draw.line(screen, color, (x, y), (x + dx, y + dy), 2)

# kutsun funktsioonid välja
drawHouse(100, 400, 300, 400, pind, red)
drawDoor(100, 400, 300, 400, pind, blue)
drawWindow(100, 400, 300, 400, pind, pink)
drawChimney(100, 400, 300, 400, pind, red)
drawSun(pind, 600, 80, 40, yellow)

pygame.display.flip()
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
