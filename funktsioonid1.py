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
