#ainult positiivsed arvud korrutamine
from sys import exception
from tkinter import N


a=float(input("A: "))
b=float(input("A: "))
if a>0 and b>0:
   print(f"Korutis võrdub: {a*b}")

#Kas a on paaris või paritu arv?
if a%2==0 and a!=0:
    print(f"Arv {a} on paaris")
elif a==0:
    print(f"Arv {a} on märamatu")
else:
    print(f"Arv {a} on paaritu")

#Ema-robot 5-, 4-, 3-, 2-, 1-
try:
    hinne=int(input("Mis hinne sai täna koolis"))
    if hinne in range(1,6):
        print("Hinne")
        if hinne==5:
            print("VH")
        elif hinne==4:
            print("H")
        elif hinne==3:
            print("R")
        else:
            print("MR")
    else:
        print("Ei ole hinne")
except Exception as e:
    print("viga: ", e)

    nimi="PYTHON"
    print(nimi.isupper())
    if nimi.isupeer():
        print("Suured tähed")
    else:
        print("Ei ole kõik suured tähed")
#Ulesanne 1
#1 Juku
nimi=input("Sisesta nimi: ")
if nimi=="JUKU":
    print("Lähme kinno!")
    vanus=int(input("Kui vana sa oled? "))
    if vanus<16:
        print("Sa ei saa vaadata 16+ filme")
    else:
        print("Sa saad vaadata 16+ filme")
else:
    print("Ma olen hõivatud! Mine kino ise!")

#2 Pinginaabrid
Nimed=["ilja, Aleksei, Marina"]
nimi1=input()
nimi2=input()
nimi3=input()
if (nimi1 in nimed) and (nimi2 in nimed) and (nimi3 in nimed) 
 and nimi1!=nimi2 and nimi2!=nimi3 and nimi1!=nimi3:
   print("Pinginaabrid")
else:
   print("Ei ole pinginaabrid")

#3
try:
    a=float(input(" Sisesta toa pikkus: "))
    b=float(input("Sisesta toa laius: "))
    if a>0 and b>0:
        pindla =a*b
        print(f"Põranda pindla on {pindala} ruutmeetri.")
        remont=input("Kas soovid põrandat vahetada?")
        if remont.lower() == "jah":
            hind=float(input("Sisesta põranda vahetuse hind:"))
            if hind>0:

                koguhind=pindla*hind
                print(f"Põranda vahetamise hind on {koguhind} eurot.")
            else:
                print("vale hind!")
        else:
            print("Remonti ei tehta")
    else:
        print("viga!")
except:
    print("Viga!")


#4
price = float(input("Sisesta toote hind: "))
if price > 700:
    discount_price = price * 0.70  
    print(f"Toote hind pärast 30% soodustust: {discount_price:.2f} eurot")
else:
    print(f"Toote hind ilma soodustuseta: {price:.2f} eurot")

#5
temperature = float(input("Sisesta temperatuur: "))

if temperature > 18:
    print("Temperatuur on üle 18 kraadi, see on soovitatav toasoojus talvel.")
else:
    print("Temperatuur on madalam kui 18 kraadi, pole soodne toasoojus.")
#6
height = float(input("Sisesta inimese pikkus (sentimeetrites): "))

if height < 160:
    print("Inimene on lühike.")
elif 160 <= height <= 175:
    print("Inimene on keskmine.")
else:
    print("Inimene on pikk.")
                       
#7
height = float(input("Sisesta inimese pikkus (sentimeetrites): "))
gender = input("Sisesta inimese sugu (mees/naine): ").lower()

if gender == "mees":
    if height < 170:
        print("Inimene on lühike.")
    elif 170 <= height <= 185:
        print("Inimene on keskmine.")
    else:
        print("Inimene on pikk.")
else:
    if height < 160:
        print("Inimene on lühike.")
    elif 160 <= height <= 170:
        print("Inimene on keskmine.")
    else:
        print("Inimene on pikk.")


#8
products = {
    "piim": random.uniform(0.5, 1.5),
    "saia": random.uniform(0.2, 1.0),
    "leib": random.uniform(0.3, 1.2)
}
product_choice = input("Mida soovite osta (piim, saia, leib)? ").lower()
quantity = int(input(f"Kui palju {product_choice} tahate osta? "))
if product_choice in products:
    total_price = products[product_choice] * quantity
    print(f"Tðekk:\n{product_choice.capitalize()}: {products[product_choice]:.2f} * {quantity} = {total_price:.2f} ")
else:
    print("Toode pole saadaval.")

