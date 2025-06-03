import pygame
import math

pygame.init()
ekraani_laius = 800
ekraani_korgus = 600
ekraan = pygame.display.set_mode((ekraani_laius, ekraani_korgus))
pygame.display.set_caption("Esimene aken")
font = pygame.font.SysFont("Arial", 60, bold=True)

KOLLANE = (255, 255, 0)
ROHELINE = (0, 255, 0)
SININE = (0, 0, 255)
LILLA = (160, 32, 240)
TUME_LILLA = (75, 0, 130)
HALL = (100, 100, 100)
VALGE = (255, 255, 255)
PRUUN = (34, 139, 34)
MUST = (0, 0, 0)

def joonista_paike(ekraan, x, y):
    for i in range(0, 360, 10):
        dx = math.cos(math.radians(i)) * 150
        dy = math.sin(math.radians(i)) * 150
        pygame.draw.line(ekraan, KOLLANE, (x, y), (x + dx, y + dy), 2)

def joonista_lill(ekraan, x, y):
    pygame.draw.circle(ekraan, TUME_LILLA, (x, y), 70)
    for i in range(19, 0, -1):
        varv = LILLA if i % 2 == 0 else TUME_LILLA
        pygame.draw.circle(ekraan, varv, (x, y), i * 4, 2)
    pygame.draw.rect(ekraan, PRUUN, (x - 7, y + 70, 15, 120))

def joonista_pilv(ekraan, x, y):
    pygame.draw.circle(ekraan, HALL, (x, y), 40)
    pygame.draw.circle(ekraan, HALL, (x + 30, y + 10), 40)
    pygame.draw.circle(ekraan, HALL, (x - 30, y + 10), 40)

töötab = True
while töötab:
    for sündmus in pygame.event.get():
        if sündmus.type == pygame.QUIT:
            töötab = False

    ekraan.fill(SININE)
    pygame.draw.rect(ekraan, ROHELINE, (0, 400, ekraani_laius, 200))  # земля

    joonista_paike(ekraan, 0, 0)
    joonista_lill(ekraan, 300, 300)
    joonista_pilv(ekraan, 600, 150)

    tekst = font.render("Tere tulemast!", True, VALGE)
    ekraan.blit(tekst, (300, 100))

    pygame.display.flip()

pygame.quit()
