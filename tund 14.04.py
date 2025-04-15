from datetime import datetime  # Импортируем модуль datetime для получения текущего года

# Главная функция
def tootajad():
    töötajad = []      # Список для хранения имен работников
    sünniaastad = []   # Список для хранения годов рождения

    # Ввод данных
    while True:
        nimi = input("Sisesta töötaja nimi (või 'stopp' lõpetamiseks): ")  # Ввод имени работника
        if nimi.lower() == 'stopp':  # Если введено 'stopp', выходим из цикла
            break
        aasta = input("Sisesta sünniaasta: ")  # Ввод года рождения
        if not aasta.isdigit():  # Проверка, что введено число
            print("Vigane aasta! Proovi uuesti.")  # Ошибка при вводе
            continue
        töötajad.append(nimi)  # Добавляем имя в список
        sünniaastad.append(int(aasta))  # Добавляем год рождения в список

    # Главное меню
    while True:
        print("\nVali tegevus:")  # Выводим меню
        print("1. Kuvada pensionärid")  # Показать пенсионеров
        print("2. Arvuta keskmine vanus")  # Посчитать средний возраст
        print("3. 10 noorimat/vanaimat töötajat")  # Показать 10 самых молодых и 10 самых старших
        print("4. Otsi töötajaid sünniaasta järgi")  # Поиск по году рождения
        print("5. Välju")  # Выход

        valik = input("Sinu valik: ")  # Ввод выбора

        # Обработка выбора пользователя
        if valik == '1':
            kuva_pensionärid(töötajad, sünniaastad)  # Показать пенсионеров
        elif valik == '2':
            arvuta_keskmine_vanus(sünniaastad)  # Посчитать средний возраст
        elif valik == '3':
            kuva_top10(töötajad, sünniaastad)  # Показать топ-10
        elif valik == '4':
            otsi_sünniaasta(töötajad, sünniaastad)  # Поиск по году рождения
        elif valik == '5':
            print("Head aega!")  # Сообщение о завершении
            break
        else:
            print("Tundmatu valik, proovi uuesti.")  # Неизвестная команда

# Функция: список пенсионеров
def kuva_pensionärid(töötajad, sünniaastad):
    aasta = datetime.now().year  # Получаем текущий год
    print("\nPensionärid (vanus 65+):")  # Заголовок
    for nimi, sünniaasta in zip(töötajad, sünniaastad):  # Объединяем имя и год рождения
        vanus = aasta - sünniaasta  # Вычисляем возраст
        if vanus >= 65:  # Проверка: пенсионный возраст
            print(f"{nimi} - {vanus} aastat")  # Вывод пенсионеров

# Функция: средний возраст
def arvuta_keskmine_vanus(sünniaastad):
    aasta = datetime.now().year  # Текущий год
    vanused = [aasta - aasta_s for aasta_s in sünniaastad]  # Список возрастов
    keskmine = sum(vanused) / len(vanused)  # Среднее арифметическое
    print(f"\nTöötajate keskmine vanus: {keskmine:.1f} aastat")  # Вывод среднего возраста

# Функция: 10 самых молодых и старых работников
def kuva_top10(töötajad, sünniaastad):
    aasta = datetime.now().year  # Текущий год
    vanused = [(nimi, aasta - sünniaasta) for nimi, sünniaasta in zip(töötajad, sünniaastad)]  # Список кортежей (имя, возраст)
    
    vanused_sorditud = sorted(vanused, key=lambda x: x[1])  # Сортируем по возрасту (по возрастанию)

    print("\n10 noorimat töötajat:")  # Заголовок для самых молодых
    for nimi, vanus in vanused_sorditud[:10]:  # Первые 10 элементов (молодые)
        print(f"{nimi} - {vanus} aastat")

    print("\n10 vanimat töötajat:")  # Заголовок для самых старых
    for nimi, vanus in vanused_sorditud[-10:][::-1]:  # Последние 10 элементов (старшие), но в обратном порядке
        print(f"{nimi} - {vanus} aastat")

# Функция: поиск по году рождения
def otsi_sünniaasta(töötajad, sünniaastad):
    aasta = input("Sisesta sünniaasta, mida otsida: ")  # Ввод года для поиска
    if not aasta.isdigit():  # Проверка правильности ввода
        print("Vigane sisend!")  # Сообщение об ошибке
        return
    aasta = int(aasta)
    print(f"\nTöötajad, kes on sündinud aastal {aasta}:")  # Заголовок
    leitud = False  # Флаг, найден ли кто-то
    for nimi, synn in zip(töötajad, sünniaastad):  # Проходим по списку
        if synn == aasta:  # Если совпадает
            print(nimi)  # Выводим имя
            leitud = True
    if not leitud:
        print("Ei leitud töötajaid sellel aastal.")  # Если никто не найден

# Запуск программы
tootajad()
