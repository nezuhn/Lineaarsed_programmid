from sonastik2 import *
fail="sonad.txt"
sonad=sonad_failist(fail)
valjasta_tervitus()

while True:
    kuva_menu()
    valik = input("\nSisesta valik: ")
    if valik == "1":
        allikas, siht=vali_keelte_suund()
        sona=input(f"Sisesta s�na({allikas}) ")
        tulemus=tolkija(sonad,allikas, siht, sona)
        print(f"T�lge: {tulemus}")   
    elif valik == "2":
         lisa_sona(sonad)
    elif valik == "3":
        paranda_sona(sonad)     
    elif valik == "4":
        kuva_sonad(sonad)    
    elif valik == "5":
        testi_teadmisi(sonad) 
    elif valik == "6":
        text_to_speech() 
    elif valik == "0":
        salvesta_sonad(fail,sonad)
        break
    else:
        print("Viga! Proovi veel kord.")
