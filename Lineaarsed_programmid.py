from random import*
from sunau import AUDIO_FILE_ENCODING_ADPCM_G721
from match import*
#ulesanne1 
print("Hello world!","Hello world!", sep =",    ", end=")")

nimi = input("Mis on sinu nimi?: ")
vanus=int(input("kui vana sa oled?: "))
print(f"Tere, maailm! Tervitan sind {nimi} Sa oled {vanus} aastat vana.")
print("Tere, maailm! Tervitan sind",nimi,"Sa oled" ,vanus,"aastat vana.")
print("Tere, maailm! Tervitan sind" +nimi+"/nSa oled" +str(vanus)+"aastat vana")

#ulesanne 2
vanus  18
eesnimi = "Jaak"
pikkus = 16.5
print(f"Muutuja {vanus} on {type(vanus)}t��bi")
print(f"Muutuja {ees nimi} on {type(ees nimi)}t��bi")
print(f"Muutuja {pikkus} on {type(pikkus)}t��bi")

#ulesanne 3
kommidearv=randit(1,100)
print(f"laual on{kommidearv} kommid")
kommidv�tmud=int(input("Mitu kommi tahad �ra v�tta?"))
onj��nud=kommidearv-kommidv�tmud
print(f"laual on {onj��nud} komme")

#ulesanne4
�mberm�tt=int (input("kui suur on �mberm�t?:"))
l�bim�tt=�mberm�tt
print(f"l�bim��t on {l�bim�t}")
  
#ulesanne5
N = float(input"sisesta �ks pool")
M = float(input"sisesta teine pool")
D2 = float ((N==2)+(#==2))
        
   #ulesanne6
    aeg = float(input("Mitu tundi kulus s�iduks"))
    teepikkus=float(input("Mitu kilomeetrit s�tsid"))
    kiirus=teepikkus/aeg
    print("Sinu kiirus oli" + str(kiirus) + "km/h")

    #ulesanne7
  a1=randit(0,100)
  a2=randit(0,100)
  a3=randit(0,100)
  a4=randit(0,100)
  a5=randit(0,100)
  keskmine=(a1+a2+a3+a4+a5)/5
  print(f"Arvud olid: {a1},{a2},{a3},{a4},{a5}. Nende on keskmine on {keskmine}. ")

  #ulesanne8 
  #1
  tekst=""
     @..@
    (----)
   ( \__/ )
   ^^ "" ^^
   print(tekst)

   #2
print("     @..@")
print("    (----)")
print("   ( \__/ )")
print(""" ^^ "" ^^""")

      
     
     #ulesanne9
   a=randit(1,100)
 b=randit(1,100)
 c=randit(1,100)
 P=a+b+c
 print(f"a={a}, b={b}, c={c}, P={P}")

 #ulesanne 10
 pizza=12,9
 s�brad=randit(2,3)
 tip= pizza=10%+pizza