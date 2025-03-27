def arithmetic(arv1:float,arv2:float,tehe:str):
    """Funktsioon töötab nagu lihtne kalkulaator
    + - liitmine
    -- lahutamine
    *- korrutamine
    /- jagamine
    Kui sisend el ole järjendus[+,-,/,*],siis tagastab sõne "Tundmatu tehe"
    :param arv1: Sisend ujukomaarvu tüübina
    :param arv1: Sisend ujukomaarvu tüübina
    :param str tehe: Sisend listist[+,-,/,*]
    :rtype: var Määramata tüüp (float või str)
    """
    if tehe in ["+","-","*","/"]:
        if arv2==0 and tehe=="/":
            vastus="DIV/0"
        else:
            vastus=eval(str(arv1)+tehe+str(arv2))
    else:
        vastus="Tundmatu tehe"
    return vastus

def is_year_leap(aasta:int)->bool:
    """Liigaasta leidmine
    Tagastab True, kui aasta on liigaastaja False kui aasta on tavaline aasta
    :param int aasta:Sisend  kasutajalt
    :rtype: bool tõeväärsuses formaadis tulemus
    """
    if aasta%4==0:
        v=True
    else:
        v=False
    return v


#3
def square(külg:float)->any:
    """
    Funktsioon tagastab ruudu ümbermõtt, ruudu pindla ja diagonaal.
    Kui sisend ei ole float siis tagastab "On vaja kirjutuda float".
    :param float arv: Sisend ujukomaarvu tüübina
    :rtype:tulemus formasdis(float) S,P,d
    """
    S=külg**2
    P=4*külg
    d=(2)**(1/2)*külg
    return S,P,d

def season(param:int)->str:
    """Kirjeldage funktsioon
    :param
    :rtype:Hooajanimetus
    """
    if param in [1,2,12]:
        H="Talv"
    elif param in [3,4,5]:
        H="Kevad"
    elif param in [6,7,8]:
        H="Suvi"
    else:
        H="Sügis"
    return H

#5
def bank(summa:float,aastad;int)->float:
    """funktsioon tagastab summa , mis jääb kasutaja kontole
    on vaja kirjutada argumeendid "a" ja aastat.
    :param
    :param
    :rtype:
    """
    for aasta in range(aastad):
        summa*=1.1
    return summa

while True:
    try:
        a=float(input("Sisesta nimi:"))
        break
    except:
        print("Viga! Sisesta arv")
while True:
    try:
        years=float(input("Sisesta kui palju aastat: "))
        break
    except:
        print("Viga! Sisesta arv")
v=bank(summa,aastad)
print(v)

from random import *
#6
def is_prime(a=randit(1,10000)):
    """
    Funktsioon tagastab True or False
    :param int: Sisend randit funktsioon.
    :rtype: bool tõevärsuses formaadis tulemus
    """
    print(a)
    v=True
    for jagaja in range(2;a-1):
        if a%jagaja==0:
            v=False
    return v

#7
def date(päev:int,kuu:int,aasta;int)->bool:
    """
    Tagastab True/False kui selline kuupäev on meie kalendris.
    :param aasta(int)
    :param kuu(int)
    :param päev(int)
    :rtype: bool tõevärsuses formaadis tulemus
    """
    if päev in range(1,32) and kuu [1,3,5,7,8,10,12] and aasta>0:
        v=True
    elif päev in range(1,30) and kuu==2 and is_year_leap(aasta):
        v=True
    elif päev in range(1,29) and kuu==2 and not is_year_leap(aasta):
        v=True
    elif päev in range(1,31) and kuu [4,6,9,11] and aasta>0:
        v=True
    else:
        v=False
    return v