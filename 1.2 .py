import pygame
pygame.init()

ekraan = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Lumemees – Sinu Nimi")

VALGE = (255, 255, 255)
MUST = (0, 0, 0)
ORANZ = (255, 100, 0)

ekraan.fill(MUST)

pygame.draw.circle(ekraan, VALGE, (150, 240), 40)  
pygame.draw.circle(ekraan, VALGE, (150, 175), 30) 
pygame.draw.circle(ekraan, VALGE, (150, 125), 20)  
pygame.draw.circle(ekraan, MUST, (143, 120), 3)
pygame.draw.circle(ekraan, MUST, (157, 120), 3)

pygame.draw.polygon(ekraan, ORANZ, [(147, 130), (153, 130), (150, 145)])

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
