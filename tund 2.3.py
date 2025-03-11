print("Tere! Olen sinu uus sõber - Python!")
nimi = input("Palun sisesta oma nimi: ")
print(f"{nimi}, oi kui ilus nimi!")
kas_soovib = input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah => ")
if kas_soovib == '1':
    try:
        pikkus = int(input("Sisesta oma pikkus sentimeetrites: "))
        mass = float(input("Sisesta oma kehakaal kilogrammides: "))
        pikkus_m = pikkus / 100 
        kmi = mass / (pikkus_m ** 2)
        print(f"{nimi}! Sinu keha indeks on: {kmi.if}")
        if kmi < 16:
            hinnang = "Tervisele ohtlik alakaal"
        elif 16 <= kmi < 19:
            hinnang = "Alakaal"
        elif 20 <= kmi <= 25:
            hinnang = "Normaalkaal"
        elif 26 <= kmi <= 30:
            hinnang = "Ülekaal"
        elif 31 <= kmi <= 35:
            hinnang = "Rasvumine"
        elif 36 <= kmi <= 40:
            hinnang = "Tugev rasvumine"
        else:
            hinnang = "Tervisele ohtlik rasvumine"
        print(f"KMI hinnang: {hinnang}")
    except ValueError:
        print("Palun sisesta kehtivad numbrid! Pikkus peab olema täisarv ja kaal reaalarv.")
elif kas_soovib == '0':
    print("Kahju! See on väga kasulik info!")
else:
    print("Vale sisend! Palun sisesta 0 või 1.")
print(f"Kohtumiseni, {nimi}! Igavesti Sinu, Python!")

