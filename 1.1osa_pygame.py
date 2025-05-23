import pygame
import random

# Algseaded
pygame.init()

# Akna suurus
laius, kõrgus = 600, 500
ekraan = pygame.display.set_mode((laius, kõrgus))
pygame.display.set_caption("Tere tulemast!")

# Värvid
sinine = (135, 206, 250)
roheline = (34, 139, 34)
kollane = (255, 255, 0)
hall = (169, 169, 169)
must = (0, 0, 0)

# Pilt mesilase jaoks (veendu, et sul on mesilase pilt olemas samas kaustas)
# Kui mesilase pilti ei ole, siis asenda see joonistatud kujutisega.
try:
    mesilane_pilt = pygame.image.load("bee.png")
    mesilane_pilt = pygame.transform.scale(mesilane_pilt, (50, 50))  # Muudame suuruse sobivaks
except:
    mesilane_pilt = None  # Kui pilti ei ole, joonistame mesilase ise

# Funktsioonid
def joonista_paike(ekraan, x, y):
    # Päike: kollane ketas ja kiired
    pygame.draw.circle(ekraan, kollane, (x, y), 40)  # Päikese ketas
    for i in range(12):
        nurk = i * 30
        x1 = x + 60 * pygame.math.cos(pygame.math.radians(nurk))
        y1 = y + 60 * pygame.math.sin(pygame.math.radians(nurk))
        pygame.draw.line(ekraan, kollane, (x, y), (x1, y1), 3)

def joonista_lill(ekraan, x, y):
    # Lill: õis ja vars
    pygame.draw.circle(ekraan, (255, 105, 180), (x, y), 20)  # Õis
    pygame.draw.rect(ekraan, (0, 128, 0), (x - 5, y, 10, 60))  # Vars

def joonista_pilv(ekraan, x, y):
    # Pilv: hallid ringid
    for i in range(3):
        pygame.draw.circle(ekraan, hall, (x + i * 40, y), 30)  # Erinevates kohtades olevad ringid

def joonista_mesilane(ekraan, x, y):
    # Mesilase joonistamine (kui pilti ei ole)
    if mesilane_pilt:
        ekraan.blit(mesilane_pilt, (x, y))
    else:
        # Keha
        pygame.draw.ellipse(ekraan, (255, 255, 0), (x, y, 30, 20))
        # Tiivad
        pygame.draw.ellipse(ekraan, (255, 255, 255), (x - 10, y - 10, 40, 20))
        pygame.draw.ellipse(ekraan, (255, 255, 255), (x + 5, y - 10, 40, 20))

# Põhiprogramm
def main():
    running = True
    while running:
        ekraan.fill(sinine)  # Taustaks sinine taevas
        pygame.draw.rect(ekraan, roheline, (0, 400, laius, kõrgus))  # Muru

        # Joonista objektid
        joonista_paike(ekraan, 500, 100)  # Päike
        joonista_lill(ekraan, 100, 450)   # Lill 1
        joonista_lill(ekraan, 200, 450)   # Lill 2
        joonista_pilv(ekraan, 100, 100)   # Pilv 1
        joonista_pilv(ekraan, 400, 150)   # Pilv 2
        joonista_mesilane(ekraan, 300, 300)  # Mesilane

        # Kuvame teksti
        font = pygame.font.Font(None, 36)
        tekst = font.render("Tere tulemast!", True, must)
        ekraan.blit(tekst, (200, 20))

        # Eventide käsitlemine
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Uuenda ekraani
        pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT: break
    pygame.quit()
