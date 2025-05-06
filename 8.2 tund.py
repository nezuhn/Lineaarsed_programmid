import numpy as np
import matplotlib.pyplot as plt

# Failist lugemine
with open('maed.txt', 'r') as file:
    lines = file.readlines()

# Andmete töötlemine
nimed = []
korgused = []

for rida in lines:
    osad = rida.strip().split()
    nimi = osad[0].replace('_', ' ')  # Muudame _ tühikuks tagasi
    korgus = int(osad[1])
    nimed.append(nimi)
    korgused.append(korgus)

# Numpy abil statistika arvutamine
korgused_np = np.array(korgused)
keskmine = np.mean(korgused_np)
maksimum = np.max(korgused_np)
minimaalne = np.min(korgused_np)
summa = np.sum(korgused_np)

# Tekstina terminalis
print("Statistika maailma kõrgeimate mägede kohta:")
print(f"Keskmine kõrgus: {keskmine:.2f} m")
print(f"Kõrgeim mägi: {nimed[np.argmax(korgused_np)]} ({maksimum} m)")
print(f"Madalamaim mägi: {nimed[np.argmin(korgused_np)]} ({minimaalne} m)")
print(f"Kogukõrgus: {summa} m")

# Graafik (esialgne, sorteerimata)
plt.figure(figsize=(10, 6))
plt.bar(nimed, korgused, color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Kõrgus (m)')
plt.title('Maailma kõrgeimad mäed')
plt.tight_layout()
plt.savefig('maed_graafik.png')
plt.show()

# Lisaülesanne: sorteerimine ja uus graafik
# Sorteerime andmed kõrguse järgi kahanevalt
nimed_np = np.array(nimed)
sorteeritud_indeksid = np.argsort(korgused_np)[::-1]
nimed_sorted = nimed_np[sorteeritud_indeksid]
korgused_sorted = korgused_np[sorteeritud_indeksid]

# Sorteritud graafik
plt.figure(figsize=(10, 6))
plt.bar(nimed_sorted, korgused_sorted, color='orange')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Kõrgus (m)')
plt.title('Maailma kõrgeimad mäed (sorteeritud)')
plt.tight_layout()
plt.savefig('maed_graafik_sorted.png')
plt.show()

