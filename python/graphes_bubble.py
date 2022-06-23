import numpy as np
import matplotlib.pyplot as plt

x1_6 = np.array([2.482,2.072,2.526])
x2_6 = np.array([9.41,13.386,10.966])
x3_6 = np.array([10.73,6.138,8.12])
x4_6 = np.array([7.41,8.664,12.856])
x5_6 = np.array([6.232,6.205,6.662])

moyenne_6 = [
        (x1_6[0]+x2_6[0]+x3_6[0]+x4_6[0]+x5_6[0])/5,
        (x1_6[1]+x2_6[1]+x3_6[1]+x4_6[1]+x5_6[1])/5,
        (x1_6[2]+x2_6[2]+x3_6[2]+x4_6[2]+x5_6[2])/5
        ]

y = np.array([30,60,90])

plt.plot(y, x1_6, color='r', linewidth=0.5)
plt.plot(y, x2_6, color='r', linewidth=0.5)
plt.plot(y, x3_6, color='r', linewidth=0.5)
plt.plot(y, x4_6, color='r', linewidth=0.5)
plt.plot(y, x5_6, color='r', linewidth=0.5)
# courbes rouges pour 6 pixels


x1_12 = np.array([1.432,1.7,1.52])
x2_12 = np.array([5.586,3.387,3.032])
x3_12 = np.array([2.44,3.506,2.846])
x4_12 = np.array([2.734,3.146,2.554])
x5_12 = np.array([1.756,2.9,2.364])

moyenne_12 = [
        (x1_12[0]+x2_12[0]+x3_12[0]+x4_12[0]+x5_12[0])/5,
        (x1_12[1]+x2_12[1]+x3_12[1]+x4_12[1]+x5_12[1])/5,
        (x1_12[2]+x2_12[2]+x3_12[2]+x4_12[2]+x5_12[2])/5
        ]



plt.plot(y, x1_12, color='b', linewidth=0.5)
plt.plot(y, x2_12, color='b', linewidth=0.5)
plt.plot(y, x3_12, color='b', linewidth=0.5)
plt.plot(y, x4_12, color='b', linewidth=0.5)
plt.plot(y, x5_12, color='b', linewidth=0.5)
# courbes rouges pour 12 pixels


x1_18 = np.array([1.29,1.31,1.526])
x2_18 = np.array([1.916,2.06,2.043])
x3_18 = np.array([2.098,1.734,3.472])
x4_18 = np.array([2.432,2.098,1.959])
x5_18 = np.array([1.568,1.448,1.746])

moyenne_18 = [
        (x1_18[0]+x2_18[0]+x3_18[0]+x4_18[0]+x5_18[0])/5,
        (x1_18[1]+x2_18[1]+x3_18[1]+x4_18[1]+x5_18[1])/5,
        (x1_18[2]+x2_18[2]+x3_18[2]+x4_18[2]+x5_18[2])/5
        ]


plt.plot(y, x1_18, color='g', linewidth=0.5)
plt.plot(y, x2_18, color='g', linewidth=0.5)
plt.plot(y, x3_18, color='g', linewidth=0.5)
plt.plot(y, x4_18, color='g', linewidth=0.5)
plt.plot(y, x5_18, color='g', linewidth=0.5)
# courbes rouges pour 18 pixels


plt.plot(y,moyenne_6, linewidth=4, color='r', label="moyenne pour 6 pixels")
plt.plot(y,moyenne_12, linewidth=4, color='b', label="moyenne pour 12 pixels")
plt.plot(y,moyenne_18, linewidth=4, color='g', label="moyenne pour 18 pixels")
plt.legend()

plt.xlabel("Nombre de cibles")
plt.ylabel("Temps en secondes")


plt.title("Technique : Bubble")

plt.show()




