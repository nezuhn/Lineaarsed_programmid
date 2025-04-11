from datetime import datetime

# Главная функция
def tootajad():
    töötajad = []
    sünniaastad = []

    # Ввод данных
    while True:
        nimi = input("Sisesta töötaja nimi (või 'stopp' lõpetamiseks): ")
        if nimi.lower() == 'stopp':
            break
        aasta = input("Sisesta sünniaasta: ")
        if not aasta.isdigit():
            print("Vigane aasta! Proovi uuesti.")
            continue
        töötajad.append(nimi)
        sünniaastad.append(int(aasta))

    # Главное меню
    while True:
        print("\nVali tegevus:")
        print("1. Kuvada pensionärid")
        print("2. Arvuta keskmine vanus")
        print("3. 10 noorimat/vanaimat töötajat")
        print("4. Otsi töötajaid sünniaasta järgi")
        print("5. Välju")

        valik = input("Sinu valik: ")

        if valik == '1':
            kuva_pensionärid(töötajad, sünniaastad)
        elif valik == '2':
            arvuta_keskmine_vanus(sünniaastad)
        elif valik == '3':
            kuva_top10(töötajad, sünniaastad)
        elif valik == '4':
            otsi_sünniaasta(töötajad, sünniaastad)
        elif valik == '5':
            print("Head aega!")
            break
        else:
            print("Tundmatu valik, proovi uuesti.")

# Функция: список пенсионеров
def kuva_pensionärid(töötajad, sünniaastad):
    aasta = datetime.now().year
    print("\nPensionärid (vanus 65+):")
    for nimi, sünniaasta in zip(töötajad, sünniaastad):
        vanus = aasta - sünniaasta
        if vanus >= 65:
            print(f"{nimi} - {vanus} aastat")

# Функция: средний возраст
def arvuta_keskmine_vanus(sünniaastad):
    aasta = datetime.now().year
    vanused = [aasta - aasta_s for aasta_s in sünniaastad]
    keskmine = sum(vanused) / len(vanused)
    print(f"\nTöötajate keskmine vanus: {keskmine:.1f} aastat")

# Функция: 10 самых молодых/старых
def kuva_top10(töötajad, sünniaastad):
    aasta = datetime.now().year
    vanused = [(nimi, aasta - sünniaasta) for nimi, sünniaasta in zip(töötajad, sünniaastad)]
    
    vanused_sorditud = sorted(vanused, key=lambda x: x[1])  # сортировка по возрасту
    print("\n10 noorimat töötajat:")
    for nimi, vanus in vanused_sorditud[:10]:
        print(f"{nimi} - {vanus} aastat")

    print("\n10 vanimat töötajat:")
    for nimi, vanus in vanused_sorditud[-10:][::-1]:
        print(f"{nimi} - {vanus} aastat")

# Функция: поиск по году рождения
def otsi_sünniaasta(töötajad, sünniaastad):
    aasta = input("Sisesta sünniaasta, mida otsida: ")
    if not aasta.isdigit():
        print("Vigane sisend!")
        return
    aasta = int(aasta)
    print(f"\nTöötajad, kes on sündinud aastal {aasta}:")
    leitud = False
    for nimi, synn in zip(töötajad, sünniaastad):
        if synn == aasta:
            print(nimi)
            leitud = True
    if not leitud:
        print("Ei leitud töötajaid sellel aastal.")

# Запуск
tootajad()

