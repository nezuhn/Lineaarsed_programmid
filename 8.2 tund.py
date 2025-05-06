import numpy as np
import matplotlib.pyplot as plt

# Failist lugemine
with open('maed.txt', 'r') as file:
    lines = file.readlines()

# Andmete t��tlemine
nimed = []
korgused = []

for rida in lines:
    osad = rida.strip().split()
    nimi = osad[0].replace('_', ' ')  # Muudame _ t�hikuks tagasi
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
print("Statistika maailma k�rgeimate m�gede kohta:")
print(f"Keskmine k�rgus: {keskmine:.2f} m")
print(f"K�rgeim m�gi: {nimed[np.argmax(korgused_np)]} ({maksimum} m)")
print(f"Madalamaim m�gi: {nimed[np.argmin(korgused_np)]} ({minimaalne} m)")
print(f"Koguk�rgus: {summa} m")

# Graafik (esialgne, sorteerimata)
plt.figure(figsize=(10, 6))
plt.bar(nimed, korgused, color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.ylabel('K�rgus (m)')
plt.title('Maailma k�rgeimad m�ed')
plt.tight_layout()
plt.savefig('maed_graafik.png')
plt.show()

# Lisa�lesanne: sorteerimine ja uus graafik
# Sorteerime andmed k�rguse j�rgi kahanevalt
nimed_np = np.array(nimed)
sorteeritud_indeksid = np.argsort(korgused_np)[::-1]
nimed_sorted = nimed_np[sorteeritud_indeksid]
korgused_sorted = korgused_np[sorteeritud_indeksid]

# Sorteritud graafik
plt.figure(figsize=(10, 6))
plt.bar(nimed_sorted, korgused_sorted, color='orange')
plt.xticks(rotation=45, ha='right')
plt.ylabel('K�rgus (m)')
plt.title('Maailma k�rgeimad m�ed (sorteeritud)')
plt.tight_layout()
plt.savefig('maed_graafik_sorted.png')
plt.show()

