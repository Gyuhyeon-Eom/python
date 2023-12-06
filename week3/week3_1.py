import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(0,1,10)

y = np.random.normal(0,1,10)
sizes = np.random.uniform(10,100,10)

colors = np.random.uniform(0,1,10)

plt.scatter(x,y, s=sizes, c=colors)
plt.colorbar()
plt.show()

x = np.arange(7) + 0.5
y = np.random.uniform(1,9,len(x))

plt.bar(x,y, width=1, edgecolor = 'white')
plt.xlabel("days")
plt.ylabel("hours")
plt.show()

from vpython import*

s = sphere(pos =vec(1,0,0), radius=0.1)