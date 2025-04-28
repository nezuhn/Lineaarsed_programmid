import os
import json
from funktsioonid import *

# Faili nimi, kus kontaktid salvestatakse
fail = "kontaktid.json"

# Kui fail ei eksisteeri, siis loome selle
if not os.path.exists(fail):
    with open(fail, 'w') as f:
        json.dump([], f)

# Loeme kontaktid failist
kontaktid = loe_kontaktid(fail)

while True:
    print("\nTelefoniraamat:")
    print("1. Lisa kontakt")
    print("2. Kuvage kõik kontaktid")
    print("3. Otsi kontakt nime järgi")
    print("4. Kustuta kontakt")
    print("5. Muuda kontakt")
    print("6. Sorteeri kontaktid")
    print("7. Saada e-kiri")
    print("8. Välju")

    valik = input("Valige tegevus: ")

    if valik == '1':
        lisa_kontakt(fail)
    elif valik == '2':
        kuva_kontaktid(fail)
    elif valik == '3':
        otsi_kontakt(fail)
    elif valik == '4':
        kustuta_kontakt(fail)
    elif valik == '5':
        muuda_kontakt(fail)
    elif valik == '6':
        sorteeri_kontaktid(fail)
    elif valik == '7':
        saada_email(fail)
    elif valik == '8':
        print("Programmi lõpetamine.")
        break
    else:
        print("Vale valik, proovige uuesti.")

