from tkinter import *
from tkinter import messagebox

kontaktid = []

teema = "hele"

valged_varvid = {
    "bg": "#f0f0f0",
    "entry_bg": "white",
    "text_color": "black",
    "button_bg": "#f0f0f0",
    "button_active_bg": "#d9d9d9"
}

tumedad_varvid = {
    "bg": "#2e2e2e",
    "entry_bg": "#4d4d4d",
    "text_color": "white",
    "button_bg": "#3a3a3a",
    "button_active_bg": "#5a5a5a"
}

varvid = valged_varvid.copy()

def uuenda_teema():
    global varvid
    if teema == "hele":
        varvid = valged_varvid
    else:
        varvid = tumedad_varvid
    
    aken.configure(bg=varvid["bg"])
    content_frame.configure(bg=varvid["bg"])
    
    for widget in content_frame.winfo_children():
        if isinstance(widget, Label):
            widget.configure(bg=varvid["bg"], fg=varvid["text_color"])
        elif isinstance(widget, Entry):
            widget.configure(bg=varvid["entry_bg"], fg=varvid["text_color"], highlightbackground="#FFB6C1", highlightcolor="#FF1493")
        elif isinstance(widget, Button):
            if widget == btn_tühjenda:
                widget.configure(bg=varvid["button_bg"], fg="red", activebackground="#FFC0C0")
            elif widget == btn_arv or widget == btn_vaheta_teemat:
                widget.configure(bg=varvid["button_bg"], fg="blue", activebackground=varvid["button_active_bg"])
            else:
                widget.configure(bg=varvid["button_bg"], fg=varvid["text_color"], activebackground=varvid["button_active_bg"])
    
    box.configure(bg=varvid["entry_bg"], fg=varvid["text_color"])

def vaheta_teemat():
    global teema
    teema = "tume" if teema == "hele" else "hele"
    uuenda_teema()

def lisa_kontakt():
    nimi = entry_nimi.get()
    telefon = entry_telefon.get()
    email = entry_email.get()
    asukoht = entry_asukoht.get()
    if nimi and telefon and email and asukoht:
        kontaktid.append({
            "nimi": nimi,
            "telefon": telefon,
            "email": email,
            "asukoht": asukoht
        })
        messagebox.showinfo("OK", "Kontakt lisatud.")
        kuva_kontaktid()
    else:
        messagebox.showerror("Viga", "Täida kõik väljad!")

def kuva_kontaktid():
    box.delete(0, END)
    for kontakt in kontaktid:
        box.insert(END, f"{kontakt['nimi']} | {kontakt['telefon']} | {kontakt['email']} | {kontakt['asukoht']}")

def otsi_kontakt():
    nimi = entry_nimi.get().strip()
    for kontakt in kontaktid:
        if kontakt["nimi"].lower() == nimi.lower():
            messagebox.showinfo("Leitud",
                                f'Nimi: {kontakt["nimi"]}\nTelefon: {kontakt["telefon"]}\nEmail: {kontakt["email"]}\nAsukoht: {kontakt["asukoht"]}')
            return
    messagebox.showerror("Viga", "Kontakti ei leitud.")

def kustuta_kontakt():
    nimi = entry_nimi.get()
    for kontakt in kontaktid:
        if kontakt["nimi"].lower() == nimi.lower():
            kontaktid.remove(kontakt)
            messagebox.showinfo("OK", "Kontakt kustutatud.")
            kuva_kontaktid()
            return
    messagebox.showerror("Viga", "Kontakti ei leitud.")

def tühjenda_kontaktid():
    if messagebox.askyesno("Kinnita", "Kas soovid kustutada kõik kontaktid?"):
        kontaktid.clear()
        kuva_kontaktid()

def naita_arv_kontakte():
    messagebox.showinfo("Kontaktide arv", f"Kontaktide arv on: {len(kontaktid)}")

def sorteeri_nime_jargi():
    kontaktid.sort(key=lambda k: k["nimi"][0].lower() if k["nimi"] else "")
    kuva_kontaktid()

# Функция валидации: разрешить только буквы (русские и латинские)
def ainult_tähed(new_text):
    if new_text == "":
        return True
    return all(ch.isalpha() or ch.isspace() for ch in new_text)  # можно добавить пробелы, если нужно

# GUI
aken = Tk()
aken.title("Telefoniraamat")
aken.geometry("1300x600")

content_frame = Frame(aken, bg=varvid["bg"], bd=0)
content_frame.pack(anchor="w", padx=20, pady=15)

font_label = ("Times New Roman", 14, "italic")
font_entry = ("Times New Roman", 14, "normal")
font_button = ("Times New Roman", 12, "italic")

Label(content_frame, text="Nimi", font=font_label, fg=varvid["text_color"], bg=varvid["bg"]).grid(row=0, column=0, sticky="w", pady=5)

validate_nimi = content_frame.register(ainult_tähed)
entry_nimi = Entry(content_frame, font=font_entry, width=20, fg=varvid["text_color"], bg=varvid["entry_bg"],
                   highlightthickness=2, highlightbackground="#FFB6C1", highlightcolor="#FF1493", bd=0,
                   validate="key", validatecommand=(validate_nimi, '%P'))
entry_nimi.grid(row=1, column=0, sticky="w", pady=5)

Label(content_frame, text="Telefon", font=font_label, fg=varvid["text_color"], bg=varvid["bg"]).grid(row=0, column=1, sticky="w", padx=10, pady=5)
entry_telefon = Entry(content_frame, font=font_entry, width=20, fg=varvid["text_color"], bg=varvid["entry_bg"],
                      highlightthickness=2, highlightbackground="#FFB6C1", highlightcolor="#FF1493", bd=0)
entry_telefon.grid(row=1, column=1, sticky="w", padx=10, pady=5)

Label(content_frame, text="E-post", font=font_label, fg=varvid["text_color"], bg=varvid["bg"]).grid(row=0, column=2, sticky="w", pady=5)
entry_email = Entry(content_frame, font=font_entry, width=25, fg=varvid["text_color"], bg=varvid["entry_bg"],
                    highlightthickness=2, highlightbackground="#FFB6C1", highlightcolor="#FF1493", bd=0)
entry_email.grid(row=1, column=2, sticky="w", pady=5)

Label(content_frame, text="Asukoht", font=font_label, fg=varvid["text_color"], bg=varvid["bg"]).grid(row=0, column=3, sticky="w", padx=10, pady=5)
entry_asukoht = Entry(content_frame, font=font_entry, width=20, fg=varvid["text_color"], bg=varvid["entry_bg"],
                      highlightthickness=2, highlightbackground="#FFB6C1", highlightcolor="#FF1493", bd=0)
entry_asukoht.grid(row=1, column=3, sticky="w", padx=10, pady=5)

button_frame = Frame(aken, bg=varvid["bg"])
button_frame.pack(pady=10)

btn_lisa = Button(button_frame, text="Lisa kontakt", command=lisa_kontakt, font=font_button, width=15,
                  bg=varvid["button_bg"], fg=varvid["text_color"], activebackground=varvid["button_active_bg"])
btn_lisa.pack(side=LEFT, padx=5)

btn_kuva = Button(button_frame, text="Kuva kontaktid", command=kuva_kontaktid, font=font_button, width=15,
                  bg=varvid["button_bg"], fg=varvid["text_color"], activebackground=varvid["button_active_bg"])
btn_kuva.pack(side=LEFT, padx=5)

btn_otsi = Button(button_frame, text="Otsi kontakti", command=otsi_kontakt, font=font_button, width=15,
                  bg=varvid["button_bg"], fg=varvid["text_color"], activebackground=varvid["button_active_bg"])
btn_otsi.pack(side=LEFT, padx=5)

btn_kustuta = Button(button_frame, text="Kustuta kontakt", command=kustuta_kontakt, font=font_button, width=15,
                     bg=varvid["button_bg"], fg=varvid["text_color"], activebackground=varvid["button_active_bg"])
btn_kustuta.pack(side=LEFT, padx=5)

btn_tühjenda = Button(button_frame, text="Tühjenda kõik", command=tühjenda_kontaktid, font=font_button, width=15,
                      bg=varvid["button_bg"], fg="red", activebackground="#FFC0C0")
btn_tühjenda.pack(side=LEFT, padx=5)

btn_arv = Button(button_frame, text="Kontaktide arv", command=naita_arv_kontakte, font=font_button, width=15,
                 bg=varvid["button_bg"], fg="blue", activebackground=varvid["button_active_bg"])
btn_arv.pack(side=LEFT, padx=5)

btn_vaheta_teemat = Button(button_frame, text="Vaheta teemat", command=vaheta_teemat, font=font_button, width=15,
                            bg=varvid["button_bg"], fg=varvid["text_color"], activebackground=varvid["button_active_bg"])
btn_vaheta_teemat.pack(side=LEFT, padx=5)

btn_sorteeri_nimi = Button(button_frame, text="Sorteeri nime järgi", command=sorteeri_nime_jargi, font=font_button, width=15,
                           bg=varvid["button_bg"], fg=varvid["text_color"], activebackground=varvid["button_active_bg"])
btn_sorteeri_nimi.pack(side=RIGHT, padx=5)

box = Listbox(aken, height=10, width=115, font=("Times New Roman", 12), fg=varvid["text_color"], bg=varvid["entry_bg"])
box.pack(padx=20, pady=10)

aken.

configure(bg=varvid["bg"])
aken.mainloop()
