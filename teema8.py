import matplotlib.pyplot as plt
import numpy as np

# x=np.arange(-10,10,1) #-10,-9,-8....10
# Y=2*x**2-4*x+5
# plt.figure(facecolor="yellow")
# plt.plot(x,y)
# plt.xlabel("X")
# plt.ylabel("y=2*x**2-4*x+5")
# plt.title("Graafik")
# plt.grid()
# plt.savefig("graafik.png")
# plt.show()

# x = [1, 2, 3, 4, 5]
# y = [10, 20, 25, 30]
# plt.plot(x, y, linestyle='--', marker='D', color='red', markersize=10, label="Laskuv joon")  # Katkendjoo
# plt.title("Lihtne graafik")
# plt.xlabel("X-telg")
# plt.ylabel("Y-telg")
# plt.show()

# plt.scatter(x, y, color="lightblue", label="Punktidest diagramm")
# plt.legend()
# plt.show()

# plt.bar(x, y, color="orange", label="Tulpdiagramm")
# plt.legend()
# plt.show()

# plt.hist(x, y, color="#97fcc7", label="Histogram")
# plt.show()

# plt.pie(x, y)
# plt.show()

plt.figure(figsize=(10, 6))
plt.title("Очки")

# 1
x1 = np.linspace(-9, -1, 400)
y1 = -(1/16)*(x1 + 5)**2 + 2
plt.plot(x1, y1, color='black')

# 2
x2 = np.linspace(1, 9, 400)
y2 = -(1/16)*(x2 - 5)**2 + 2
plt.plot(x2, y2, color='black')

# 3
x3 = np.linspace(-9, -1, 400)
y3 = (1/4)*(x3 + 5)**2 - 3
plt.plot(x3, y3, color='black')

# 4
x4 = np.linspace(1, 9, 400)
y4 = (1/4)*(x4 - 5)**2 - 3
plt.plot(x4, y4, color='black')

# 5
x5 = np.linspace(-9, -6, 200)
y5 = -(x5 + 7)**2 + 5
plt.plot(x5, y5, color='black')

# 6
x6 = np.linspace(6, 9, 200)
y6 = -(x6 - 7)**2 + 5
plt.plot(x6, y6, color='black')

# 7
x7 = np.linspace(-1, 1, 200)
y7 = -0.5 * x7**2 + 1.5
plt.plot(x7, y7, color='black')

# Сетка и соси
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.show()