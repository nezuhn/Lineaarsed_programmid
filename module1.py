#7
N=1
for i in range(4):
    N*=10
    N+=randit(0,9)
    print(N)

#6 

#5
N = int(input("N: "))

for i in range(N):
    for j in range(N):
        if i == j or i + j == N -1
            print("X", end=" ")
        else:
            print("O", end=" ")
print()


#4
for i in range(1, 11):
    print(i)

print("\nТаблица умножения:")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")



#3
for küsime_nr in range(10):
    a=randit(1,50)
    b=randit(1,50)
    õige_vastus=a+b
    print(f"{a}+{b}="))
    p=0
    õ=0
    vastus=0
    while p<5 or vastus!=õige_vastus
        vastus=int(input(f"{a}+{b}="))
        if vastus==õige_vastus: 
            print("tubli!!")
            õ+=1
        p+=1
    print(f"Õige vastus: {õige_vastus}")
print("vastus on õige")     





#2
summa=0
j=0
while true:
    while True
        try:
            a=float(input("a: "))
            break
        except:
            print("viga!")
    summa+=a
    j+=1
    if j==10: break
print(f"Arvude summa: {summa}")
#----
summa = 0
while true:
    number = input("Sisesta arv (vajuta Enter lõpetamiseks): ")
    if number == "": break
    try:
        number=float(number)
        summa += number
    except:
        print("viga")
        print(f"Arvude summa: {summa}")



a=0
while a==0
    print (a)
    a=int(input("a: "))
while true:
    print(a)
    a=int(input("a: "))
    if a==100: break
print()
for i in range(0,10,1):
    print(f"{i+1}. samm")
print()
for i in range(1, 11):
    print(f"{i}. samm")


#1
while true:
    try:
        nimi=input("Mis on sinu nimi")
        if nimi.isalpha(): break
    except:
    print("Viga!")
while true:
    try:
        nimi=(input("Mitu korda tervitada"))
        if k>0: break
    except:
         print("Viga!")
#1. variant
orint("while true")
i=0
while true:
    i+=1
    print(f"Ole tervitatud, {nimi}, {i}. korda.")
    if i==k: break
#3. variant
print("while tingimusega")
i=0
while i>k:
    i+=1
    print(f"Ole tervitatud, {nimi}, {i}. korda.")
#3. variant
print("For")
for i in range(1,k+1):
    print(f"Ole tervitatud, {nimi}, {i}. korda.")



#ulesanne2
from keyboard import *