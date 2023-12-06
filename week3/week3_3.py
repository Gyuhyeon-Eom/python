import numpy as np
import matplotlib.pyplot as plt

wavelength = 15.0
k = np.pi*2/wavelength
side = 100
points = 500
spacing = side/points

A = np.empty([points, points], float)
for i in range(points):
    y = spacing*i
    for j in range(points):
        x = spacing*j
        r = np.sqrt(x**2+y**2)
        A[i,j] = np.sin(k*r)
plt.imshow(A, origin="lower", extent=[0,side,0,side])
plt.colorbar()
plt.show()

'''
x = np.random.normal(0,1,10)
y = np.random.normal(0,1,10)
sizes = np.random.uniform(10,100,10)

colors = np.random.uniform(0,1,10)

plt.subplot(1,3,1)
plt.scatter(x,y, s=sizes, c=colors)
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')

x1 = np.arange(7) + 0.5
y1 = np.random.uniform(1,9,len(x1))

plt.subplot(1,3,2)
plt.bar(x1,y1, width=1 ,edgecolor='white')
plt.xlabel('days')
plt.ylabel('hours')

x2 = np.random.normal(0, 1, 10000)

plt.subplot(1,3,3)
plt.hist(x2, bins=15, edgecolor='white')
plt.xlabel('x')
plt.ylabel('frequency')
plt.show()
'''