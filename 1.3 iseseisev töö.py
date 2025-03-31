import math  # Импортируем модуль math для математических операций

print("Характеристики квадрата")  # Сообщение для квадрата
try:
    a = int(input('Введите длину стороны квадрата => '))  # Вводим длину стороны квадрата
    if a > 0:  # Проверяем, что длина стороны больше 0
        S = a**2  # Площадь квадрата (сторона^2)
        print(f"Площадь квадрата: {S}")
        
        P = 4 * a  # Периметр квадрата (4 * сторона)
        print(f"Периметр квадрата: {P}")
        
        di = a * math.sqrt(2)  # Диагональ квадрата (сторона * √2)
        print(f"Диагональ квадрата: {round(di, 2)}")  # Округляем до 2 знаков после запятой
    else:
        print("Сторона не может быть <= 0")  # Если сторона <= 0, выводим ошибку
except:
    print("Ошибка: введите целое число!")  # Если введено не число

print("Характеристики прямоугольника")  # Сообщение для прямоугольника
try:
    b = int(input("Введите длину 1-й стороны прямоугольника => "))  # Вводим первую сторону
    c = int(input("Введите длину 2-й стороны прямоугольника => "))  # Вводим вторую сторону
    
    if b <= 0 or c <= 0:  # Проверяем, что стороны положительные
        print("Стороны должны быть положительными числами.")
    else:
        S = b * c  # Площадь прямоугольника (сторона1 * сторона2)
        print(f"Площадь прямоугольника: {S}")
        
        P = 2 * (b + c)  # Периметр прямоугольника (2 * (сторона1 + сторона2))
        print(f"Периметр прямоугольника: {P}")
        
        di = math.sqrt(b**2 + c**2)  # Диагональ прямоугольника по теореме Пифагора
        print(f"Диагональ прямоугольника: {round(di)}")  # Округляем до целого числа
except:
    print("Ошибка: введите числовые значения!")  # Если введены не числа

print("Характеристики окружности")  # Сообщение для окружности
try:
    r = int(input("Введите радиус окружности => "))  # Вводим радиус окружности
    
    if r <= 0:  # Проверяем, что радиус больше 0
        print("Радиус должен быть положительным числом.")
    else:
        d = 2 * r  # Диаметр окружности (2 * радиус)
        print(f"Диаметр окружности: {d}")
        
        S = math.pi * r**2  # Площадь окружности (π * радиус^2)
        print(f"Площадь окружности: {round(S)}")  # Округляем до целого числа
        
        C = 2 * math.pi * r  # Длина окружности (2 * π * радиус)
        print(f"Длина окружности: {round(C)}")  # Округляем до целого числа
except:
    print("Ошибка: введите числовые значения!")  # Если введены не числа
