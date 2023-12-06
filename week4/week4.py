import numpy as np
import matplotlib.pyplot as plt

#Bisection Method
x = np.arange(0, 2*np.pi, 0.01)
y = np.sin(x) -0.5

plt.plot(x, y, x, np.zeros(len(x)))
plt.show

eps = 1E-8
def f(x) :
    return np.sin(x)-0.5

x1 = 0
x2 = np.pi/2.0 

steps =[]
x3_list = []
step = 0
while ( (x2 - x1) > eps):
    x3 = (x1 + x2) / 2.0
    if (f(x1)*f(x3) < 0.0):
        x2 = x3
    else:
        x1 = x3

    steps.append(step)
    x3_list.append(x3)
    step+=1
plt.plot(steps, x3_list)
plt.xlabel("step")
plt.ylabel("x3")
plt.yscale("log")
plt.show
#print(x3)
#print(np.pi/6)




#Newton Method