#t�� 4.4
#1
from re import T
from string import *
vokaali=["a","e","u","o","i","�","�","�","�"]
konsonanti="qwrtpsdfghklzxcvbnmj"
numbrid=digits
m�rkid=punctuation
tekst=input=input("Sisend (s�na v�i lause): ").lower()
tekst_list=list(tekst)
if tekst_list.index(" ")>0:
    print("See on lause")
    for s in tekst_list:
        if s in vokaali:
            v+=1
        elif s in konsonanti:
            k+=1
        elif s in numbrid:
            n+=1
        elif s in m�rkid:
            m+=1
        elif s==" ":
            t+=1
    print(f"V: {v}\nK: {k}\nN: {n}\nM: {m}\nT: {t}")
else:
    print(f"Kokku on {len(tekst_list)}")






s�ne="Programmeerimine"
print(s�ne)
list_s�ne=list(s�ne)
print(list_s�ne)
print(f"Viies t�ht: {list_s�ne[4]}")
print(f"S�ne on {len(s�ne)} t")
#append
elemendid=[]
for i in range(5):
    elemendid.append(input(f"{i+1}. element: "))
print(elemendid)
for e in elemendid:
    print(e)
#extend
list_s�ne.extend(elemendid)
print(list_s�ne)
print(elemendid)
#insert
elemendid.insert(0,"A")
print(elemendid)
#remove
elemendid.remove("A")
print(elemendid)
#pop
eleemendid.pop(0)
elemedid.pop()
print(elemendid)
#index
ind=list_s�ne.index("r")
print(" T�ht r on {ind}-indeksiga")
#count
k=list_s�ne.count("r")
print(f"T�ht r kohtume {k} korda s�nas {s�ne}")
#sort
list_s�ne.sort(reverse=True)
print(list_s�ne)
#reverse
list_s�ne.reverse()
print(list_s�ne)
#copy
list_s�ne2=list_s�ne.copy()
#clear
list_s�ne2.clear()
print(list_s�ne2)