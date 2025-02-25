from random import*
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
print(f"Muutuja {vanus} on {type(vanus)}tüübi")
print(f"Muutuja {ees nimi} on {type(ees nimi)}tüübi")
print(f"Muutuja {pikkus} on {type(pikkus)}tüübi")

#ulesanne 3
kommidearv=randit(1,100)
print(f"laual on{kommidearv} kommid")
kommidvõtmud=int(input("Mitu kommi tahad ära võtta?"))
onjäänud=kommidearv-kommidvõtmud
print(f"laual on {onjäänud} komme")

#ulesanne4
ümbermõtt=int (input("kui suur on ümbermõt?:"))
läbimõtt=ümbermõtt
print(f"läbimõõt on {läbimõt}")
  
#ulesanne5
N = float(input"sisesta üks pool")
M = float(input"sisesta teine pool")
D2 = float ((N==2)+(#==2))
