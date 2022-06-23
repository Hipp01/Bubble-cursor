import numpy as np
import matplotlib.pyplot as plt

x1_6 = np.array([2.27,2.946,2.432])
x2_6 = np.array([6.662,5.748,5.37])
x3_6 = np.array([3.654,4.998,4.159])
x4_6 = np.array([3.464,5.372,6.956])
x5_6 = np.array([4.894,4.558,2.31])

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


x1_12 = np.array([1.458,1.566,1.296])
x2_12 = np.array([2.15,2.854,2.756])
x3_12 = np.array([1.996,2.684,2.03])
x4_12 = np.array([2.404,2.842,2.606])
x5_12 = np.array([1.326,2.032,1.972])


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


x1_18 = np.array([1.824,1.42,1.296])
x2_18 = np.array([1.934,1.694,1.892])
x3_18 = np.array([1.918,1.628,2.014])
x4_18 = np.array([2.044,2.16,2.244])
x5_18 = np.array([1.644,1.43,1.346])

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


plt.title("Technique : Rope")

plt.show()



