from datetime import*
from calendar import*
tana=date.today()
print(f"Tere  ! Täna on {tana}")
# 27/12/2022
tana = tana.strftime("%d/%m/%Y")
print(tana1)

# December 27, 2022
tana = tana.strftime("%B %d, %Y")
print(tana2)

# 12/27/22
tana = tana.strftime("%m/%d/%y")
print(tana3)

# Dec-27-2022
tana = tana.strftime("%b-%d-%Y")
print(tana4)

päev=tana.day
kuu=tana.month
aasta=tana.year

print(f"Päev on {päev}, \nKuu on {kuu}, \nAasta on {aasta}")
paevad=monthrage(2025,2)[1]
onjaanud=paevad-päevprint(f"Kuu lõpuni on jäänud {onjaanud} päevad")


print(f"Päev on {päev}, \nKuu on {kuu}, \nAasta on {aasta}")
months=monthrange(2025,1)[1]
monthsleft=months-kuu
print(f"Till the end of the year {onjaanud} months are left") 
try:
    sunnipäev=input("Sünnipäev: 12.24.2007")
    sp=datetime.strptime(sünnipäev,"%Y-%m-%d")
    print(sp)
    vanus_aastades=tana.year-sp.year
    vanus_kuudes=vanus_aastades*12 
    print("vastus: Vanus {vanus_aastades} aastad")
except:
        print("Sa pead YYYY-MM-DD foramt kasutada sisestamisel")


  #ulesanne 2
  #sulgude kasutamine
  print("a=3 + 8/ (4-2) * 4")
  a=3 + 8 / (4 - 2) *4
  print(a)
  print("a=(3+8)/ (4-2) *4")
  a=(3 + 8) / (4 - 2) *4
  print(a)