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