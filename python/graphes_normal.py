import numpy as np
import matplotlib.pyplot as plt

x1_6 = np.array([1.468,1.915,2.66])
x2_6 = np.array([3.754,2.468,3.38])
x3_6 = np.array([2.776,2.974,4.47])
x4_6 = np.array([2.22,3.228,2.829])
x5_6 = np.array([2.124,2.62,2.738])

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


x1_12 = np.array([1.142,1.764,1.712])
x2_12 = np.array([1.904,2.52,2.024])
x3_12 = np.array([2.064,3.692,3.458])
x4_12 = np.array([2.248,1.984,2.754])
x5_12 = np.array([1.544,2.384,2.266])

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


x1_18 = np.array([1.336,1.134,1.232])
x2_18 = np.array([1.739,1.624,1.536])
x3_18 = np.array([1.972,1.844,1.852])
x4_18 = np.array([1.996,1.649,1.806])
x5_18 = np.array([1.702,1.606,1.45])

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

plt.title("Technique : Normal")

plt.show()



