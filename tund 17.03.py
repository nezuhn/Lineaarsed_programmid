#t�� 4.4
#1
from re import T
from string import *
vokaali=["a","e","u","o","i","�","�","�","�"]
konsonanti="qwrtpsdfghklzxcvbnmj"
numbrid=digits
m�rkid=punctuation
tekst=input=input("Sisend (s�na v�i lause): ").lower()
tekst_list=list(tekst)
if tekst_list.index(" ")>0:
    print("See on lause")
    for s in tekst_list:
        if s in vokaali:
            v+=1
        elif s in konsonanti:
            k+=1
        elif s in numbrid:
            n+=1
        elif s in m�rkid:
            m+=1
        elif s==" ":
            t+=1
    print(f"V: {v}\nK: {k}\nN: {n}\nM: {m}\nT: {t}")
else:
    print(f"Kokku on {len(tekst_list)}")






s�ne="Programmeerimine"
print(s�ne)
list_s�ne=list(s�ne)
print(list_s�ne)
print(f"Viies t�ht: {list_s�ne[4]}")
print(f"S�ne on {len(s�ne)} t")
#append
elemendid=[]
for i in range(5):
    elemendid.append(input(f"{i+1}. element: "))
print(elemendid)
for e in elemendid:
    print(e)
#extend
list_s�ne.extend(elemendid)
print(list_s�ne)
print(elemendid)
#insert
elemendid.insert(0,"A")
print(elemendid)
#remove
elemendid.remove("A")
print(elemendid)
#pop
eleemendid.pop(0)
elemedid.pop()
print(elemendid)
#index
ind=list_s�ne.index("r")
print(" T�ht r on {ind}-indeksiga")
#count
k=list_s�ne.count("r")
print(f"T�ht r kohtume {k} korda s�nas {s�ne}")
#sort
list_s�ne.sort(reverse=True)
print(list_s�ne)
#reverse
list_s�ne.reverse()
print(list_s�ne)
#copy
list_s�ne2=list_s�ne.copy()
#clear
list_s�ne2.clear()
print(list_s�ne2)

#2
names = []
for _ in range(5):
    name = input("Sisesta nimi: ")
    names.append(name)
names.sort()
print("T�hestikulises j�rjekorras nimed:", names)
print("Viimati lisatud nimi:", names[-1])

change_name = input("Kas soovid m�nda nime muuta? (jah/ei): ").strip().lower()
if change_name == "jah":
    old_name = input("Sisesta nimi, mida soovid muuta: ")
    if old_name in names:
        new_name = input("Sisesta uus nimi: ")
        names[names.index(old_name)] = new_name
        names.sort()  
        print("Uus nimekiri:", names)
    else:
        print("Seda nime ei leitud loendist.")
opilased = ["Juhan", "Kati", "Mario", "Mario", "Mati", "Mati"]

unique_opilased = list(set(opilased))

print("Kordumatud nimed:", unique_opilased)

vanused = [25, 18, 22, 20, 30, 21, 19]

kogus = len(vanused)
suurim = max(vanused)
vikesim = min(vanused)
summa = sum(vanused)
keskmine = summa / kogus

print(f"Vanuste kogus: {kogus}")
print(f"Suurim vanus: {suurim}")
print(f"V�ikseim vanus: {vikesim}")
print(f"Vanuste summa: {summa}")
print(f"Keskmine vanus: {keskmine:.2f}")


#3
arvud = [3, 5, 8, 12, 15, 20]
for arv in arvud:
    print('*' * arv)

#4
def kontrolli_postiindeks(postiindeks):
    if len(postiindeks) != 5 or not postiindeks.isdigit():
        return "Postiindeks peab olema 5 numbrit pikk."
    maakond = postiindeks[0]

    if maakond == "1":
        maakond_nimi = "Tallinn"
    elif maakond == "2":
        maakond_nimi = "Narva, Narva-J�esuu"
    elif maakond == "3":
        maakond_nimi = "Kohtla-J�rve"
    elif maakond == "4":
        maakond_nimi = "Ida-Virumaa, L��ne-Virumaa, J�gevamaa"
    elif maakond == "5":
        maakond_nimi = "Tartu linn"
    elif maakond == "6":
        maakond_nimi = "Tartumaa, P�lvamaa, V�rumaa, Valgamaa"
    elif maakond == "7":
        maakond_nimi = "Viljandimaa, J�rvamaa, Harjumaa, Raplamaa"
    elif maakond == "8":
        maakond_nimi = "P�rnumaa"
    elif maakond == "9":
        maakond_nimi = "L��nemaa, Hiiumaa, Saaremaa"
    else:
        return "Tundmatu maakond."
    if maakond in ["1", "2", "3"]:
        teade = "Osta j��ge kodus!"
    else:
        teade = "Kandke maske!"

    return f"Postiindeks {postiindeks} kuulub maakonda: {maakond_nimi}. {teade}"

postiindeks = input("Palun sisestage postiindeks: ")
tulemus = kontrolli_postiindeks(postiindeks)
print(tulemus)

#7
def sorteerimine(nimekiri, kasvav=True):
    return sorted(nimekiri, key=abs, reverse=not kasvav)

nimekiri = input("Palun sisestage numbrid, eraldatud komadega: ")
nimekiri = [int(x) for x in nimekiri.split(",")]

valik = input("Kas soovite sorteerida kasvavalt (k) v�i kahanevalt (d)? ").lower()

if valik == 'k':
    sorteeritud_nimekiri = sorteerimine(nimekiri, kasvav=True)
    print("Kasvavalt sorteeritud nimekiri:", sorteeritud_nimekiri)
elif valik == 'd':
    sorteeritud_nimekiri = sorteerimine(nimekiri, kasvav=False)
    print("Kahanevalt sorteeritud nimekiri:", sorteeritud_nimekiri)
else:
    print("Vale valik. Palun valige 'k' v�i 'd'.")

#5
def vaheta_elemendid(loend, vahetus_arv):
    if vahetus_arv > len(loend) // 2:
        print("Vahetus arv ei tohi �letada poole loendi pikkusest.")
        return loend

    for i in range(vahetus_arv):
        loend[i], loend[-(i + 1)] = loend[-(i + 1)], loend[i]

    return loend

loend = [1, 2, 3, 4, 5, 6]

vahetus_arv = int(input("Palun sisestage, kui palju elemente soovite vahetada: "))

if len(loend) < 2:
    print("Loendis peab olema v�hemalt 2 elementi.")
else:
    muudetud_loend = vaheta_elemendid(loend, vahetus_arv)
    print("Muudetud loend:", muudetud_loend)