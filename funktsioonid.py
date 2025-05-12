import json
import smtplib
from email.mime.text import MIMEText
import os
import json 

fili_nimi = "kontaktid.json"

def loe_kontaktid_failist():
    if not os.path.exists(faili_nimi):
        return []
    with open(faili_nimi, "r", encoding="utf-8") as f:
        return json.load(f)

def salvesta_kontaktid_faili(kontaktid):
    with open(faili_nimi, "w", encoding="utf-8") as f:
        json.dump(kontaktid, f, ensure_ascii=False, indent=4)

def lisa_kontakt(kontaktid, nimi, telefon, email):
    kontaktid.append({"nimi": nimi, "telefon": telefon, "email": email})

# Kontaktide lugemine failist
def loe_kontaktid(fail):
    with open(fail, 'r') as f:
        return json.load(f)

# Kontaktide kirjutamine faili
def kirjuta_kontaktid(fail, kontaktid):
    with open(fail, 'w') as f:
        json.dump(kontaktid, f)

# Uue kontakti lisamine
def lisa_kontakt(fail):
    nimi = input("Sisesta kontakt, nimi: ")
    telefon = input("Sisesta telefoninumber: ")
    email = input("Sisesta e-posti aadress: ")

    kontakt = {
        "nimi": nimi,
        "telefon": telefon,
        "email": email
    }

    kontaktid = loe_kontaktid(fail)
    kontaktid.append(kontakt)
    kirjuta_kontaktid(fail, kontaktid)
    print("Kontakt lisatud.")

# Kõikide kontaktide kuvamine
def kuva_kontaktid(fail):
    kontaktid = loe_kontaktid(fail)
    if kontaktid:
        for kontakt in kontaktid:
            print(f"{kontakt['nimi']} | {kontakt['telefon']} | {kontakt['email']}")
    else:
        print("Kontaktide nimekiri on tühi.")

# Kontakti otsimine nime järgi
def otsi_kontakt(fail): 
    return [k for k in kontaktid if nimi.lower() in k['nimi'].lower()]
   

# Kontakti kustutamine
def kustuta_kontakt(fail):
    nimi = input("Sisesta kustutatava kontakti nimi: ")
    kontaktid = loe_kontaktid(fail)
    kontaktid = [k for k in kontaktid if k['nimi'].lower() != nimi.lower()]
    kirjuta_kontaktid(fail, kontaktid)
    print(f"Kontakt {nimi} kustutatud.")

# Kontakti muutmine
def muuda_kontakt(fail):
    nimi = input("Sisesta muudetava kontakti nimi: ")
    kontaktid = loe_kontaktid(fail)
    
    for kontakt in kontaktid:
        if kontakt['nimi'].lower() == nimi.lower():
            kontakt['nimi'] = input("Sisesta uus nimi: ")
            kontakt['telefon'] = input("Sisesta uus telefoninumber: ")
            kontakt['email'] = input("Sisesta uus e-posti aadress: ")
            kirjuta_kontaktid(fail, kontaktid)
            print("Kontakt muudetud.")
            return
    print("Kontakti ei leitud.")

# Kontaktide sorteerimine
def sorteeri_kontaktid(fail):
    valik = input("Sorteri järgi (nimi, telefon, email): ").lower()
    kontaktid = loe_kontaktid(fail)
    
    if valik == "nimi":
        kontaktid.sort(key=lambda k: k['nimi'])
    elif valik == "telefon":
        kontaktid.sort(key=lambda k: k['telefon'])
    elif valik == "email":
        kontaktid.sort(key=lambda k: k['email'])
    
    kirjuta_kontaktid(fail, kontaktid)
    print("Kontaktid on sorteeritud.")

# E-kirja saatmine (boonus)
def saada_email(fail):
    email = input("Sisesta saadetava kontakti e-posti aadress: ")
    kontaktid = loe_kontaktid(fail)
    
    for kontakt in kontaktid:
        if kontakt['email'].lower() == email.lower():
            msg = MIMEText("Tere, see on test e-kiri!")
            msg['Subject'] = "Test e-kiri"
            msg['From'] = "teie.email@example.com"
            msg['To'] = kontakt['email']

            try:
                with smtplib.SMTP('smtp.example.com', 587) as server:
                    server.starttls()
                    server.login("teie.email@example.com", "parool")
                    server.sendmail("teie.email@example.com", kontakt['email'], msg.as_string())
                print("E-kiri saadetud!")
            except Exception as e:
                print(f"Viga e-kirja saatmisel: {e}")
            return
    print("Kontakti e-post ei leitud.")

