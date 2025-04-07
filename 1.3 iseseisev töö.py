import math  # Impordime math mooduli

print("Ruudu omadused")  # Teade ruudu kohta
try:
    a = int(input('Sisestage ruudu külje pikkus => '))  # Sisestame ruudu külje pikkuse
    if a > 0:  # Kontrollime, et külje pikkus on suurem kui 0
        S = a**2  # Ruudu pindala (külg^2)
        print(f"Ruudu pindala: {S}")
        
        P = 4 * a  # Ruudu perimeeter (4 * külg)
        print(f"Ruudu perimeeter: {P}")
        
        di = a * math.sqrt(2)  # Ruudu diagonaal (külg * √2)
        print(f"Ruudu diagonaal: {round(di, 2)}")  # Ümarame kahe komakoha täpsusega
    else:
        print("Külg ei saa olla <= 0")  # Kui külg <= 0, kuvame vea
except:
    print("Viga: sisestage täisarv!")  # Kui sisestatakse mitte-arv

print("Õigekumeriku omadused")  # Teade ristküliku kohta
try:
    b = int(input("Sisestage 1. külje pikkus ristkülikule => "))  # Sisestame esimese külje pikkuse
    c = int(input("Sisestage 2. külje pikkus ristkülikule => "))  # Sisestame teise külje pikkuse
    
    if b <= 0 or c <= 0:  # Kontrollime, et küljed on positiivsed
        print("Küljed peavad olema positiivsed numbrid.")
    else:
        S = b * c  # Ristküliku pindala (külg1 * külg2)
        print(f"Ristküliku pindala: {S}")
        
        P = 2 * (b + c)  # Ristküliku perimeeter (2 * (külg1 + külg2))
        print(f"Ristküliku perimeeter: {P}")
        
        di =  (b**2 + c**2)  # Ristküliku diagonaal Pythagorase teoreemi järgi
        print(f"Ristküliku diagonaal: {round(di)}")  # Ümarame täisarvuni
except:
    print("Viga: sisestage arvväärtused!")  # Kui sisestatakse mitte-arv

print("Ringjoone omadused")  # Teade ringjoone kohta
try:
    r = int(input("Sisestage ringjoone raadius => "))  # Sisestame ringjoone raadiuse
    
    if r <= 0:  # Kontrollime, et raadius on positiivne
        print("Raadius peab olema positiivne number.")
    else:
        d = 2 * r  # Ringjoone diameeter (2 * raadius)
        print(f"Ringjoone diameeter: {d}")
        
        S = math.pi * r**2  # Ringjoone pindala (π * raadius^2)
        print(f"Ringjoone pindala: {round(S)}")  # Ümarame täisarvuni
        
        C = 2 * math.pi * r  # Ringjoone ümbermõõt (2 * π * raadius)
        print(f"Ringjoone ümbermõõt: {round(C)}")  # Ümarame täisarvuni
except:
    print("Viga: sisestage arvväärtused!")  # Kui sisestatakse mitte-arv
