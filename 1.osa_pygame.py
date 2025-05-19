import pygame
def paike():
    x=200
    y=0
    for i in range(30):
        pygame.draw.line(ekraani_pind, kollane, (0, 0), (x, y), 5)
        x-=7
        y+=7
        if i in range (10, 20):
            pygame.dra.line(ekraani_pind, kollane, (0, 0), (x+i, y+i), 5)
        else:
            pygame.draw.line(ekraani_pind, kollane, (0, 0), (x, y), 5)
pygame.init()
kollane=[255, 255, 0]
punane=[255, 0, 0]
sinine=[0, 0, 255]
hall=[128, 128, 128]
pruun=[139, 69, 19]

ekraani_pind=pygame.display.set_mode((880, 600))
pygame.display.set_caption("Pygame aken")
ekraani_pind.fill(hall)
pygame.draw.rect(ekraani_pind, kollane (100, 100, 200, 100))
pygame.draw.circle(ekraani_pind, punane, (400, 300), 50)
pygame.draw.polygon(ekraani_pind, kollane, [(600, 100), (700, 100), (650, 50)])
pygame.draw.line(ekraani_pind, kollane, (100, 500), (700, 500), 10)

pilt1=pygame.image.load("bee.png")
pilt1=pygame.transform.scale(pilt1, (100, 100))
ekraani_pind.blit(pilt1, (300, 400 ))
ekraani_pind.blit(pilt1, (500, 400 ))
# tekst
pygame.font.SysFont('Arrial', 50)
sõnum="Tere tulemast!"
teksti_lisamine=font.render(sõnum, True, punane)
ekraani_pind.blit(teksti_lisamine, (600, 400))
pygame.diplay.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT: break
    pygame.quit