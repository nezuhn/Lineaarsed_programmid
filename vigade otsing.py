from math import *
print("Ruudu karakteristikud")
try:
    a=int(input('Sisesta ruudu k�lje pikkus => '))
    if a>0:
        S=a**2
        print("Ruudu pindala", S)
        P=4*a
        print("Ruudu �mberm��t", P)
        di=a*sqrt(2)
        print("Ruudu diagonaal", round(di,2))
    else:
        print("k�lg ei saa olla 0 v�i v�hem.")
except:
    print("Viga! sisesta ainult t�isarvud!")
    

print("Ristk�liku karakteristikud")
try:
    b=int(input("Sisesta ristk�liku 1. k�lje pikkus => "))
    c=int(input("Sisesta ristk�liku 2. k�lje pikkus => "))
    if b>0 and c>0:
        S=b*c
        print("Ristk�liku pindala", S)
        P=2*(b+c)
        print("Ristk�liku �mberm��t", P)
        di=sqrt(b*2+c*2)
        print("Ristk�liku diagonaal", round(di))
    else:
        print("b ja c ei saa olla 0 v�i v�hem.")
except:
    print("Viga! sisesta ainult t�isarvud!")


print("Ringi karakteristikud")
try:
    r=int(input("Sisesta ringi raadiusi pikkus => "))
    if r>0:
        d=2*r
        print("Ringi l�bim��t", d)
        S=pi*r**2
        print("Ringi pindala", round(S))
        C=2*pi*r
        print("Ringjoone pikkus", round(C))
    else:
        print("r ei saa olla 0 v�i v�hem.")
except:
    print("Viga! sisesta ainult t�isarvud!")