def kontroll_number(kood):
    kaal1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    summa = sum(int(kood[i]) * kaal1[i] for i in range(10))
    jake = summa % 11

    if jake != 10:
        return jake
    else:
        kaal2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
        summa = sum(int(kood[i]) * kaal2[i] for i in range(10))
        jake = summa % 11
        if jake == 10:
            return 0
        return jake

def check_code(kood):
    if len(kood) != 11:
        return False
    if kood[0] not in '123456':
        return False
    try:
        day = int(kood[5:7])
        month = int(kood[3:5])
        year = int(kood[1:3]) + 1900 if int(kood[0]) in [1, 2] else int(kood[1:3]) + 2000
    except ValueError:
        return False
    
    if not (1 <= month <= 12 and 1 <= day <= 31):
        return False
    
    if int(kood[10]) != kontroll_number(kood):
        return False
    
    return True

def get_gender(kood):
    if kood[0] in '135':
        return 'мужчина'
    elif kood[0] in '246':
        return 'женщина'
    return 'неизвестно'

def get_birthdate(kood):
    day = kood[5:7]
    month = kood[3:5]
    year = int(kood[1:3]) + 1900 if int(kood[0]) in [1, 2] else int(kood[1:3]) + 2000
    return f'{day}.{month}.{year}'

def get_hospital(kood):
    city_code = int(kood[7:10])
    hospitals = {
        range(1, 11): 'Kuressaare Haigla',
        range(11, 20): 'Tartu Ülikooli Naistekliinik, Tartumaa, Tartu',
        range(21, 221): 'Ida-Tallinna Keskhaigla, Pelgulinna sünnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla',
        range(221, 271): 'Ida-Viru Keskhaigla (Kohtla-Järve, endine Jõhvi)',
        range(271, 371): 'Maarjamõisa Kliinikum (Tartu), Jõgeva Haigla',
        range(371, 421): 'Narva Haigla',
        range(421, 471): 'Pärnu Haigla',
        range(471, 491): 'Pelgulinna Sünnitusmaja (Tallinn), Haapsalu haigla',
        range(491, 521): 'Järvamaa Haigla (Paide)',
        range(521, 571): 'Rakvere, Tapa haigla',
        range(571, 601): 'Valga Haigla',
        range(601, 651): 'Viljandi Haigla',
        range(651, 701): 'Lõuna-Eesti Haigla (Võru), Põlva Haigla'
    }
    
    for range_code, hospital in hospitals.items():
        if city_code in range_code:
            return hospital
    return 'Неизвестная больница'

ikoodid = []
arvud = []

while True:
    kood = input("Введите личный код (или 'exit' для завершения): ")
    if kood.lower() == 'exit':
        break
    
    if check_code(kood):
        gender = get_gender(kood)
        birthdate = get_birthdate(kood)
        hospital = get_hospital(kood)
        
        if gender == 'женщина':
            ikoodid.append(f"Это {gender}, ее день рождения {birthdate} и место рождения {hospital}")
        else:
            ikoodid.append(f"Это {gender}, его день рождения {birthdate} и место рождения {hospital}")
    else:
        arvud.append(kood)

ikoodid_men = [x for x in ikoodid if 'мужчина' in x]
ikoodid_women = [x for x in ikoodid if 'женщина' in x]
ikoodid_sorted = ikoodid_women + ikoodid_men

arvud_sorted = sorted(arvud)

print("\nСписок правильных личных кодов:")
for kood in ikoodid_sorted:
    print(kood)

print("\nСписок неправильных личных кодов:")
for kood in arvud_sorted:
    print(kood)

