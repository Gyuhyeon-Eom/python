import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

address = 'http://url.kr/mjq5wh'
data = np.laodtxt(address)

x = data[:,0]
y = data[:,1]

Sxy = np.sum(x*y)
Sxx = np.sum(x*x)
H = Sxy/Sxx

print(H)

plt.plot(x,y, "x", label = "data")
plt.plot(x,H*x, label ="H*d")
plt.xlabel("d (Mpc)")
plt.ylabel("v (m/s)")
plt.legend()
plt.show()
