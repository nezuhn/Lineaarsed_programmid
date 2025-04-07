
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
    """ Самая высокая зарплата и кто её получает
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
    """Самая большая зарплата и кто её получает
    """
    suurim=max(p)
    k=i.count(suurim)
    if k>0:
     for j in range(k):
        ind=p.index(suurim)
        print(f"Saab kätte {i[ind]}")
        ind=ind+1

def Sorteerimine_kasvav(p:list,i:list)-> any:
    """
    """
    v=input("Vali märk: > (kasvav) või < (kahanev)")
    for n in range(0,len(i)):
        for m in range(n,len(i)):
            if eval(str(p[n])+v+str(p[m])):
                p[n],p[m]=p[m],p[n]
                i[n],i[m]=i[m],i[n]
    return p,i
