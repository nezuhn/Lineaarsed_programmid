#ulesanne 1
from datetime import*
from calendar import*
tana=date.today()
print(f"Tere  ! Täna on {tana}")
# 27/12/2022
tana = tana.strftime("%d/%m/%Y")
print(tana1)

# December 27, 2022
tana = tana.strftime("%B %d, %Y")
print(tana2)

# 12/27/22
tana = tana.strftime("%m/%d/%y")
print(tana3)

# Dec-27-2022
tana = tana.strftime("%b-%d-%Y")
print(tana4)

päev=tana.day
kuu=tana.month
aasta=tana.year

print(f"Päev on {päev}, \nKuu on {kuu}, \nAasta on {aasta}")
paevad=monthrage(2025,2)[1]
onjaanud=paevad-päevprint(f"Kuu lõpuni on jäänud {onjaanud} päevad")


print(f"Päev on {päev}, \nKuu on {kuu}, \nAasta on {aasta}")
months=monthrange(2025,1)[1]
monthsleft=months-kuu
print(f"Till the end of the year {onjaanud} months are left") 
try:
    sunnipäev=input("Sünnipäev: 12.24.2007")
    sp=datetime.strptime(sünnipäev,"%Y-%m-%d")
    print(sp)
    vanus_aastades=tana.year-sp.year
    vanus_kuudes=vanus_aastades*12 
    print("vastus: Vanus {vanus_aastades} aastad")
except:
    print("Sa pead YYYY-MM-DD foramt kasutada sisestamisel")


  #ulesanne 2
  #sulgude kasutamine
print("a=3 + 8/ (4-2) * 4")
a=3 + 8 / (4 - 2) *4
print(a)
print("a=(3+8)/ (4-2) *4")
a=(3 + 8) / (4 - 2) *4
print(a)


  #ulesanne 3
try:
    R=float(input("Sisesta R, kus R on ringi raadius:"))
    # ==, !=, <, >, <=, >=
   if R<=0:
       print("Nulliga ja neg. arvudega ei ole mõtte töötada!")
   else:
       Ringi_S=round(pi*R**2,2)
       Ringi_P=round(2*pi*R,2)
       Ruudsu_S=2*R*2*R
       Ruudu_P=4*2*R
       print(f"Ringi_S= {Ringi_S}\nRingi_P= {Ringi_P}\nRuudu_S {Ruudsu_S}\nRuudu_P= {Ruudu_P}")
except:
    print("Sisesta ainult arvud!!!")


#ulesanne4
Earth_Radius = float(637800000)
Coin_Radius =float(25.75)
Earth_D=2+Earth_Radius
Earth_C=pi+Earth_D
Coins_Per_Earth=Earth_C/Coin_Radius
print(f"It would take {round(Coins_Per_Earth)}")

#ulesanne6
t="""
Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
Kas sa tea, kes olid seal?

Rong see sõitis tuut tuut tuut, 
piilupart oli rongijuht.
rattad tegid kill koll koll,
kill koll koll ha kill koll kill
"""
print(t.upper())

#ulesanne 5 
a="kill-koll". capitalize()
b="killadi-koll ". capitalize()
print(a, a, b, a, a, b, a, a, a, a)

#ulesanne 7
a=float("Sisesta ristiküliku esimene külje pikkus.")
b=float("Sisesta ristkülikuteine külje pikkus.")
ümbermõtt=2(a+b)
pindla=b
print(f"Ristküliku ümbernõtt on {ümbermõtt} ja pindla on {pindla}")

#ulesanne 8
liitrid=float ("Sisesta tangitud kütuse liitrid")
kilomeetrid=float("Sisesta äbitud kilomeetrid")
try:
    if R<=0:
        print("Nulliga ja neg. arvudega ei ole mõtte töötada!")
    else:
        kesk_tarbimine=l/k*100

#ulesanne 9
kiirus_kmh=29.9
minutid=float(input("Sisesta aeg rulluisutamisel:"))
vahemaa_km=round({kiirus_kmh}/60)

#ulesanne 10 
minutid_kasutajalt=int(input("Aeg minutides:"))
tunnid=minutid_kasutajalt//60
minutid=minutid_kasutajalt%60
print("vastus".center(20,"*"))