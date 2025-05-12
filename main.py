import tkinter as tk
from tkinter import messagebox
import funktsioonid as f
kontaktid=f.loe_kontaktid_failist()
def kuva_kontaktid():
    tekstikast.delete("1.0", "end")
    for kontakt in kontaktid:
        tekstikast.insert("end", f"{kontakt['nimi']} | {kontakt['telefon']} | {kontakt['email']}\n")

def lisa_kontakt():
    nimi = nimi_entry.get()
    telefon = telefon_entry.get()
    email = email_entry.get()
    if nimi and telefon and email:
        f.lisa_kontakt(kontaktid, nimi, telefon, email)
        f.salvesta_kontaktid_faili(kontaktid)
        messagebox.showinfo("Edu", "Kontakt lisatud.")
        nimi_entry.delete(0, 'end')
        telefon_entry.delete(0, 'end')
        email_entry.delete(0, 'end')
        kuva_kontaktid()
    else:
        messagebox.showwarning("Tühjad väljad", "Täida kõik väljad.")

def otsi_kontakti_gui():
    nimi = nimi_entry.get()
    tulemused = f.otsi_kontakt(kontaktid, nimi)

    if tulemused:
        kontakt = tulemused[0]
        otsingu_viide.set(kontakt["nimi"])

        nimi_entry.delete(0, 'end')
        nimi_entry.insert(0, kontakt["nimi"])
        telefon_entry.delete(0, 'end')
        telefon_entry.insert(0, kontakt["telefon"])
        email_entry.delete(0, 'end')
        email_entry.insert(0, kontakt["email"])
        tekstikast.delete("1.0", 'end')
        tekstikast.insert("end", f"leitud: {kontakt['nimi']} | {kontakt ['telefon']} | {kontakt['email']}\n")
    else:
        messagebox.showinfo("Tulemus puudub", "Kontakti ei leitud.")

def kustuta_kontakt_gui():
    nimi = nimi_entry.get()
    if f.kustuta_kontakt(kontaktid, nimi):
        f.salvesta_kontaktid_faili(kontaktid)
        messagebox.showinfo("Kustutatud", f"'{nimi}' kustutati.")
        kuva_kontaktid()
    else:
        messagebox.showwarning("Ei leitud", "Kontakti ei leitud.")

def muuda_kontakt(kontaktid, vana_nimi, uus_nimi, uus_telefon, ):


def sorteeri_kontaktid(kontaktid, vaike):




