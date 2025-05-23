import random
# Словарь: Эстонский на Русский
sonastik = {'koer': 'собака', 'kass': 'кошка', 'maja': 'дом', 'auto': 'машина', 'päike': 'солнце'}
#  Перевод с эстонского на русский
def tolgi_est_rus(sona):
    # Используем .get(), чтобы избежать ошибки, если слова нет
    return sonastik.get(sona.lower(), "Ei leitud!")  # "Не найдено!"
#  Перевод с русского на эстонский
def tolgi_rus_est(sona):
    # Перебираем словарь, ищем русское слово в значениях
    for est, rus in sonastik.items(): #позволяет пройтись по словарю и получить одновременно и ключ, и его значение
        if rus == sona.lower():
            return est
    return "Ei leitud!" 
#  Добавление нового слова
def lisa_sona():
    # Запрашиваем у пользователя слово на двух языках
    est = input("Sisesta sõna eesti keeles: ").lower() 
    rus = input("Sisesta sõna vene keeles: ").lower()
    sonastik[est] = rus
    print("Sõna on lisatud!")  # "Слово добавлено!"
#  Изменение (редактирование) перевода слова
def paranda_sona():
    sona = input("Sisesta parandatav sõna: ").lower()
    if sona in sonastik:
        rus = input(f"Praegune tõlge: {sonastik[sona]}. Sisesta uus tõlge: ").lower()
        sonastik[sona] = rus
        print("Tõlge on parandatud!")  # "Перевод обновлён!"
    else:
        print("Sõna ei leitud!")  # "Слово не найдено!"
#  Проверка знаний ( тест)
def testi_teadmisi():
    print("\nTestimine algab!")  # "Начинаем тест!"
    correct = 0
    for _ in range(5): #количество поворов
        # Выбираем случайное слово на эстонском
        est_sona = random.choice(list(sonastik.keys()))
        rus = input(f"Mis on eesti sõna '{est_sona}' vene keeles?: ").lower()
        if tolgi_est_rus(est_sona) == rus:
            print("Õige!")  # "Правильно!"
            correct += 1
        else:
            print(f"Vale! Õige vastus on: {tolgi_est_rus(est_sona)}")  # "Неправильно! Правильный ответ:"
    print(f"Tulemus: {correct}/5 ({(correct / 5) * 100}%)")  # "Результат"
# Меню для пользователя
def menu():
    print("""
1. Tõlgi eesti keelest vene keelde    
2. Tõlgi vene keelest eesti keelde     
3. Lisa uus sõna                        
4. Paranda sõna                        
5. Testi teadmisi                        
6. Välju                               
""")
#1Перевод с русского на эстонский       
#2Добавить новое слово
#3Изменить перевод слова
#4Проверка знаний (тест)
#5Выход из программы
#6 выход
def main():#бесконечный цикл(меню будет повторяться, пока пользователь не выберет "6")
    while True:
        menu()  # Показываем меню
        choice = input("Vali tegevus: ")  # Запрашиваем у пользователя выбор действия (1–6)
        if choice == '1': # Перевод с эстонского на русский
            word = input("Sisesta sõna eesti keeles: ").lower()  # Вводим слово на эстонском
            print("Tõlge vene keelde:", tolgi_est_rus(word))  # Показываем перевод
        elif choice == '2': # Перевод с русского на эстонский
            word = input("Sisesta sõna vene keeles: ").lower()  # Вводим слово на русском
            print("Tõlge eesti keelde:", tolgi_rus_est(word))  # Показываем перевод
        elif choice == '3':# Добавление нового слова в словарь
            lisa_sona()  # Вызов функции, которая спрашивает два слова и добавляет в словарь
        elif choice == '4':# Изменение перевода уже существующего слова
            paranda_sona()  # Пользователь указывает слово и новый перевод словарь обновляется
        elif choice == '5': # Запуск мини-теста для проверки знаний
            testi_teadmisi()  # Будет задано 5 слов — нужно правильно перевести
        elif choice == '6':# Завершение программы
            print("Head aega!")  # Сообщение на прощание
            break  # Выход из цикла и завершение программы

        else:
            # Если введено что-то другое (не 1–6)
            print("Vale valik, proovi uuesti!")  # Сообщаем о неверном выборе и повторяем меню
    else:
            print("Vale valik, proovi uuesti!")  # "Неверный выбор, попробуйте снова!"

# Запуск программы это 
if __name__ == "__main__":
    main()
    input("\nProgramm lõppes. Vajuta Enter, et sulgeda.")  # Пауза перед закрытием

    #if __name__ == "__main__":Это условие, которое проверяет, запущен ли файл напрямую (как основная программа),
    # а не импортирован как модуль в другой файл.
   # input("\nProgramm lõppes. Vajuta Enter, et sulgeda.")
    #После завершения main(), программа покажет сообщение:
    #"Программа завершилась. Нажми Enter, чтобы закрыть.
   # Это пауза, чтобы окно не закрылось сразу
