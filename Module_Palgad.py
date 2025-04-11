
p=[]
i=[]
def Lisa_andmed(p:list,i:list):
    """Функция для добавления работника и его зарплаты
    """
    while True:
        try:
            nimi=input("Nimi: ")
            if nimi.isalpha():
                try:
                    palk=float(input("Palk:"))
                except:
                    print("Palk on arv!")
                break
                print("Andmed on lisatud")
        except:
            print("Kirjuta ainult tähede kasutades")
    p.append(palk)
    i.append(nimi)

def Kustuta_andmed(p:list,i:list):
    """ Удалить человека и его зарплату
    """
    try:
         nimi=input("Nimi: ")
         if nimi.isalpha():
             k=i.count(nimi)
             if k>0:
                 for j in range(k):
                     ind=i.index(nimi)
                     i.pop(ind)
                     p.pop(ind)
                 print("Andmed on kustutatud")
             else:
                 print("Andmed puuduvad!")
    except:
        print("Kirjuta ainult tähtede kasutades")
def Suurim_palk(p:list,i:list):
    """Самую большую зарплату и кто ее получает 
    """
    suurim=max(p)
    k=i.count(suurim)
    if k>0:
     for j in range(k):
        ind=p.index(suurim)
        print(f"Saab kätte {i[ind]}")
        ind=ind+1

def Sorteerimine_kasvav(p:list,i:list)-> any:
    """Упорядочить зарплаты в порядке возрастания и убывания вместе с именами
    """
    v=input("Vali märk: > (kasvav) või < (kahanev)")#Try except koos while true'ga
    for n in range(0,len(i)):
        for m in range(n,len(i)):
            if eval(str(p[n])+v+str(p[m])):
                p[n],p[m]=p[m],p[n]
                i[n],i[m]=i[m],i[n]
    return p,i

def Võrdsed_palgad(p:list,i:list):
    """Узнать, кто получает одинаковую зарплату, найти сколько таких людей вывести их данные на экран.
    """
    hulk=set(p)
    print(hulk)
    for palk in hulk:
        k=p.count(palk)
        if k>1:
            print(f"Palk {palk}")
            ind=p.index(palk)
            for j in range(k):
                ind=p.index(palk,ind)
                print(f"Saab kätte {i[ind]}")
                ind+=1

def palk_nime_jargi(inimesed, palgad, nimi):
    """Сделать поиск зарплаты по имени человека. Учесть, что имена могут повторяться
    """

    # Ищет зарплату по имени человека
    nimi = nimi.capitalize()  # Учитываем регистр имени
    if nimi in inimesed:
        indeks = inimesed.index(nimi)  # Находим индекс имени
        return palgad[indeks]  # Возвращаем зарплату
    else:
        print(f"{nimi} не найден в списке.")  # Если имя не найдено
        return None

def inimesed_üle_alla_summa(inimesed, palgad, summa, suurem=True):
    """ Вывести список людей(с зарплатами), кто получает больше/меньше чем указанная сумма.
    """
tulemus = []
for i, palk in enumerate(palgad):
        if suurem and palk > summa:  # Если зарплата больше заданной суммы
            tulemus.append((inimesed[i], palk))
        elif not suurem and palk < summa:  # Если зарплата меньше заданной суммы
            tulemus.append((inimesed[i], palk))
            

def top_t_inimesed(inimesed, palgad, t=3):
    """ Т самых бедных и самых богатых человека
    """
    inimesed_sorted, palgad_sorted = jargesta_palgad(inimesed, palgad, kasvasv=False)  # Сортируем по убыванию
    top_rikkad = list(zip(inimesed_sorted[:t], palgad_sorted[:t]))  # Самые богатые
    top_vaesed = list(zip(inimesed_sorted[-t:], palgad_sorted[-t:]))  # Самые бедные
    return top_rikkad, top_vaesed

def keskmine_palk(inimesed, palgad):
    """ Среднюю зарплату и имя человека ее получающего
    """
    keskmine = sum(palgad) / len(palgad)  # Средняя зарплата
    saajad = [inimesed[i] for i, palk in enumerate(palgad) if palk == keskmine]  # Люди с этой зарплатой
    return keskmine, saajad

def tulumaks(palk):
    """Вычислить зарплату, которую человек получит на руки после вычисления подоходного налога.
    """
    maks = palk * 0.2  # Налог
    netopalk = palk - maks  # Чистая зарплата
    return netopalk

def Bonus_Salary(p:list, i:list):
    """Cвоя функция по выбору. Добавляет прибавку к зарплате выбранному работнику, позваляя выбрать процент на какой зарплата увеличивается
    """
    for idx,(name,salary) in enumerate(zip(i,p),l):
        print("\nCurrent employees and their salaries:")
        print(f"{idx+1}. {name}: {salary}")
    try:
        choice=int(input("Valige töötaja:")) -1
        bonus = float(input("Kirjutage mittu protsentis palk tõuseb"))
        if 0 <=choice < len (i) and bonus > 0:
            original_salary = p[choice]
            bonus_to = bonus / 100
            bonus_salary = original_salary * bonus_to + original_salary
            print(f"New salary is: {bonus_salary}$")
        else:
            print("Valige eksisteeriv töötaja valige bonus rohkem kui 0")


    except:
        print("Error!")

def palgaotsing(p:list, i:list):
    """Funktsioon teha palgaotsing isiku nimi järgi.
    :param i:Inimeste nimekiri
    :param p: Palkade nimekiri
    :rtype:none
    """
    nimi=input("Sisesta nimi mida sa sooviks: ")
    leitud = False
    for j in range(len(i)):
        for j in range(len(i)):
            if nimi == i[j]:
                print(f"{nimi} palk on {p[j]}")
                leitud = True
    if leitud==False:
        print(f"{nimi} kohta andmeid ei leitud. ") 