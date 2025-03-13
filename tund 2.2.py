#6
try:
    küsimus = input("Kas sa tahad lahendada ruutvõrrandi? ")
    if küsimus.lower()=="jah":
        print("Võrrand: a*x**2+b*x+c=0")
        a=int(input("Sisesta arv a: "))
        b=int(input("Sisesta arv b: "))
        c=int(input("Sisesta arv c: "))
        D=b^2-4*a*c
        print(f"D={D}")
        if D>0:
            x1=(-b+sqrt(D))/2*a
            x2=(-b-sqrt(D)/2*a)
            print(f"Võrrand on lahendatud, x1={round(x1, 2)} ja x2={round(x2, 2)}")
        elif D==0:
            x=-b/(2*a)
            print(f"Võrrand on lahendatud,x={round(x, 2)}")
        elif D<0:
            print("Lahendusi pole")
    else:
        print("ok")
except:
    print("Viga")



#5
user_input = input("Sisesta väärtus: ")
if user_input.isdigit():  
    num = int(user_input) 
    print(f"Sisesta number: {num}")
    print(f"Type: täisarv")
    print(f"50% from {num} = {num * 0.5}")
elif user_input.replace('.', '', 1).isdigit() and user_input.count('.') == 1:  
    num = float(user_input)  
    print(f"Sisestatud number: {num}")
    print(f"Type: murdarv")
    print(f"70% from {num} = {num * 0.7}")
elif user_input.isalpha(): 
    print(f"Sisestatud väärtus {user_input}")
    print(f"type: tekst")
else:
    print("Sisestatud vale väärtus.")


#4
try:
päev=int(input("Sünnipäev"))
kuu=int(input("Sünnipäev"))
if (kuu==3 and päev>=21) or (kuu==4 and päev<=19):
    märk="Jäär"
elif (kuu==4 and päev>=20) or (kuu==5 and päev<=20):
    märk="Sõnn"
elif (kuu==5 and päev>=21) or (kuu==6 and päev<=21):
    märk="Kaksikud"
elif (kuu==6 and päev>=22) or (kuu==7 and päev<=22):
    märk="Vähk"
elif (kuu==7 and päev>=23) or (kuu==8 and päev<=22):
    märk="Lõvi"
elif (kuu==8 and päev>=23) or (kuu==9 and päev<=22):
    märk="Neitsi"
elif (kuu==9 and päev>=23) or (kuu==10 and päev<=22):
    märk="Kaalud"
elif (kuu==10 and päev>=23) or (kuu==11 and päev<=21):
    märk="Skorpion"
elif (kuu==11 and päev>=22) or (kuu==12 and päev<=21):
    märk="Ambur"
elif (kuu==12 and päev>=22) or (kuu==1 and päev<=19):
    märk="Kaljukits"
elif (kuu==1 and päev>=20) or (kuu==2 and päev<=18):
    märk="Veevalaja"
elif (kuu==2 and päev>=19) or (kuu==3 and päev<=20):
    märk="Kalad"
    print(märk)
except:
    print("Palun valige sinu sünnipäev")

#3
try:
    soov=input("Kas tahad dekodeerida?").lower() 
    if soov=="jah"
        try:
            nr=int(input("Päeva number: "))
            if nr in range(1,7):
                if nr==1:
                    print("Esmaspäev")
                elif nr==2:
                    print("Teisipäev")
                elif nr==3:
                    print("Kolmapäev")
                elif nr==4:
                    print("Neljapäev")
                elif nr==5
                    print("Reede")
                elif nr==6
                    print("Laupäev")
                elif nr==7
                    print("Pühapäev")
            else:
                print("Ainult 1-7")
         except:
            print("numbrid vahemikust 1-7")
except:
    print("Mul on vaja vastus Jah või Ei")







#2
try:
    nurk1=float("Esimene nurk"))
    nurk2=float("Tene nurk"))
    nurk3=float("Kolmas nurk"))
    if nurk1>0 and nurk2>0 and nurk3>0:
        print("Nurgad on positiivsed")
        if nurk1+nurk2+nurk3==180:
            print("See on kolmnurk")
            if nurk1==nurk2 and nurk2==nurk3:
                print("võrgkülgne kolmnurk")
            elif: nurk1==nurk2 or nurk2==nurk3 or nurk1==nurk3:
                print("Võrdvaarne kolmnurk")
            else:
                print("Erikülgne kolmnurk")
        else:
            print("See ei ole kolmnurk")
    else:
        print("Negatiivsed nurgad ei soobi")
except:
    print("Sisesta ujukomaarvud")





#1
try:
    arv=input("Sisesta arv:")
    if arv.isnumeric():
        arv=int(arv)
        if arv>0:
            if arv%2==0:
                print("Paaris arv")
            else:
                print("Paaritu")
        else:
            print("Negatiivne arv")
except:
    print("Kirjuta numbreid")