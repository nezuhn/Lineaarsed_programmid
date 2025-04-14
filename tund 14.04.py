from datetime import datetime  # импортируем модуль для получения текущего года

# Главная функция, где всё начинается
def tootajad():
    töötajad = []        # тут будут храниться имена работников
    sünniaastad = []     # а тут их года рождения

    # Вводим данные о работниках
    while True:
        nimi = input("Sisesta töötaja nimi (või 'stopp' lõpetamiseks): ")  # спрашиваем имя
        if nimi.lower() == 'stopp':  # если написали "stopp", то выходим из ввода
            break
        aasta = input("Sisesta sünniaasta: ")  # спрашиваем год рождения
        if not aasta.isdigit():  # если ввели не число, то ошибка
            print("Vigane aasta! Proovi uuesti.")
            continue  # просим ввести заново
        töötajad.append(nimi)            # добавляем имя в список
        sünniaastad.append(int(aasta))   # добавляем год (как число)

    # Меню с выбором действия
    while True:
        print("\nVali tegevus:")  # выводим список действий
        print("1. Kuvada pensionärid")  # показать пенсионеров
        print("2. Arvuta keskmine vanus")  # посчитать средний возраст
        print("3. 10 noorimat/vanaimat töötajat")  # топ 10 по возрасту
        print("4. Otsi töötajaid sünniaasta järgi")  # найти по году рождения
        print("5. Välju")  # выйти

        valik = input("Sinu valik: ")  # спрашиваем, что выбрать

        # В зависимости от выбора — вызываем нужную функцию
        if valik == '1':
            kuva_pensionärid(töötajad, sünniaastad)
        elif valik == '2':
            arvuta_keskmine_vanus(sünniaastad)
        elif valik == '3':
            kuva_top10(töötajad, sünniaastad)
        elif valik == '4':
            otsi_sünniaasta(töötajad, sünniaastad)
        elif valik == '5':
            print("Head aega!")  # прощание
            break  # выходим из меню
        else:
            print("Tundmatu valik, proovi uuesti.")  # если выбрали что-то странное

# Эта функция показывает пенсионеров (кому 65 лет и больше)
def kuva_pensionärid(töötajad, sünniaastad):
    aasta = datetime.now().year  # берём текущий год
    print("\nPensionärid (vanus 65+):")
    for nimi, sünniaasta in zip(töötajad, sünniaastad):  # идём по

