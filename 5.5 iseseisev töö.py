from datetime import datetime  # Импортируем модуль для работы с датой и временем

# Главная функция, с которой начинается программа
def tootajad():
    töötajad = []       # Список для хранения имён работников
    sünniaastad = []    # Список для хранения годов рождения

    # Ввод данных о работниках
    while True:
        nimi = input("Sisesta töötaja nimi (või 'stopp' lõpetamiseks): ")  # Запрашиваем имя работника
        if nimi.lower() == 'stopp':  # Если введено "stopp", выходим из цикла
            break
        aasta = input("Sisesta sünniaasta: ")  # Запрашиваем год рождения
        if not aasta.isdigit():  # Проверяем, что введённое значение — число
            print("Vigane aasta! Proovi uuesti.")  # Сообщение об ошибке
            continue  # Переход к следующей итерации
        töötajad.append(nimi)  # Добавляем имя в список
        sünniaastad.append(int(aasta))  # Добавляем год рождения (преобразованный в число)

    # Главное меню
    while True:
        print("\nVali tegevus:")  # Предлагаем действия на выбор
        print("1. Kuvada pensionärid")
        print("2. Arvuta keskmine vanus")
        print("3. 10 noorimat/vanaimat töötajat")
        print("4. Otsi töötajaid sünniaasta järgi")
        print("5. Välju")

        valik = input("Sinu valik: ")  # Получаем выбор пользователя

        # В зависимости от выбора вызываем соответствующую функцию
        if valik == '1':
            kuva_pensionärid(töötajad, sünniaastad)
        elif valik == '2':
            arvuta_keskmine_vanus(sünniaastad)
        elif valik == '3':
            kuva_top10(töötajad, sünniaastad)
        elif valik == '4':
            otsi_sünniaasta(töötajad, sünniaastad)
        elif valik == '5':
            print("Head aega!")  # Прощаемся
            break  # Выход из меню
        else:
            print("Tundmatu valik, proovi uuesti.")  # Обработка неправильного ввода

# Функция для отображения пенсионеров (65 лет и старше)
def kuva_pensionärid(töötajad, sünniaastad):
    aasta = datetime.now().year  # Получаем текущий год
    print("\nPensionärid (vanus 65+):")
    for nimi, sünniaasta in zip(töötajad, sünniaastad):
        vanus = aasta - sünniaasta  # Считаем возраст
        if vanus >= 65:
            print(f"{nimi} - {vanus} aastat")  # Выводим имя и возраст

# Функция для вычисления среднего возраста
def arvuta_keskmine_vanus(sünniaastad):
    aasta = datetime.now().year  # Текущий год
    vanused = [aasta - aasta_s for aasta_s in sünniaastad]  # Список возрастов
    keskmine = sum(vanused) / len(vanused)  # Средний возраст
    print(f"\nTöötajate keskmine vanus: {keskmine:.1f} aastat")

# Функция для отображения 10 самых молодых и 10 самых старых работников
def kuva_top10(töötajad, sünniaastad):
    aasta = datetime.now().year
    # Создаём список кортежей (имя, возраст)
    vanused = [(nimi, aasta - sünniaasta) for nimi, sünniaasta in zip(töötajad, sünniaastad)]
    
    # Сортируем по возрасту (от младшего к старшему)
    vanused_sorditud = sorted(vanused, key=lambda x: x[1])

    # Вывод 10 самых молодых работников
    print("\n10 noorimat töötajat:")  # Молодые
    for i in range(10):  # Проходим по первым 10 элементам
        nimi, vanus = vanused_sorditud[i]
        print(f"{nimi} - {vanus} aastat")

    # Вывод 10 самых старых работников
    print("\n10 vanimat töötajat:")  # Пожилые
    for i in range(1, 11):  # Проходим по последним 10 элементам, начиная с конца
        nimi, vanus = vanused_sorditud[-i]
        print(f"{nimi} - {vanus} aastat")

# Функция для поиска работников по году рождения
def otsi_sünniaasta(töötajad, sünniaastad):
    aasta = input("Sisesta sünniaasta, mida otsida: ")  # Запрос года
    if not aasta.isdigit():  # Проверка на число
        print("Vigane sisend!")
        return
    aasta = int(aasta)
    print(f"\nTöötajad, kes on sündinud aastal {aasta}:")
    leitud = False  # Флаг для проверки, были ли найдены совпадения
    for nimi, synn in zip(töötajad, sünniaastad):
        if synn == aasta:
            print(nimi)
            leitud = True
    if not leitud:
        print("Ei leitud töötajaid sellel aastal.")  # Если не найдено

# Запуск программы
tootajad()
