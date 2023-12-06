import numpy as np
import matplotlib.pyplot as plt

g = 9.8
N = 100
Np = N+1
a = 0 
b = 10
h = (b-a)/N
target = 1e-10

x = 500*np.ones(Np,float)

x[0] = 0
x[N] = 0
xp = np.zeros(Np,float)
gh2 = g*h*h
flag = True
counter = 0
divider = 10

while flag:
  flag = False
  counter += 1

  for i in range(1,N):
    xp[i] = 0.5*(x[i+1]+x[i-1]+gh2)
    if flag == False:
      if abs (xp[i]-x[i])>target:

        flag = True

      x = 1.0*xp
      if counter%divider ==0:
        plt.plot(np.arange(a,b+h,h),x)
        divider *= 10 

plt.plot(np.arange(a,b+h,h),x)
plt.xlabel("time(s)")
plt.ylabel("height(m)")
plt.show
