from Teema5_kasutajate_fun import *
#try except!
while True:
    try:
        a=float(input("Arv1: "))
        break
    except:
        print("Viga! Sisesta arv")
while True:
    try:
        b=float(input("Arv2: "))
        break
    except:
        print("Viga! Sisesta arv")
while True:
    try:
    t=input("Tehe: ")
    break
except:
    print("Viga! Sisesta ((/);(*);(-);(+)")
vastus=arithmetic(a,b,t)
print(vastus)

vastus=arithmetic(float(input("Arv1: ")),float(input("Arv2: ")),input("Tehe: "))
print(vastus)


#is_year_leap funktsioon kasutamine
aasta=int(input("Mis aasta tahad kontrollida?"))
if aasta>0:
    v=is_year_leap(aasta)
    print(v)
    if v:
        print(f"{aasta} on liigaasta")
    else:
        print(f"{aasta} ei ole liigaasta")


#square() kasutamine
#Kontroll while true ja try except...
a=float(input("Ruudu külg= "))

S,P,d=square(a)


#6



#7
try:
    päev=int(input("Sisesta päev: "))
    kuu=int(input("Sisesta kuu: "))
    aasta=int(input("Sisesta aasta: "))
    v=date(päev,kuu,aasta)
    print(v)
except:
    print("Viga!")