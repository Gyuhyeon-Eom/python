'''
과제1)
리만제타함수가 (pi)^2/6에 가까워 지는가
과제2)
사진참고
'''
import numpy as np
import matplotlib.pyplot as plt
import math

money = 1
month = 0
n=1
x_arr = []

for n in range(1,13):
    x = (1+(1/n))**(n)
    x_arr.append(x)
    # money += money*x
    # month += 1
    print(x)
plt.plot(range(n),x_arr)
plt.axhline(math.e,0,13)
plt.xlim([0,13])
plt.show()
#-----------------------------
'''
N = 10000
p = 6/(np.pi**2)

for n in range(N):
    zeta = (1/n)**2
'''
    
N = 10000
x_arr = []

for n in range(1,N+1):
    x = (1+1/n)**n
    x_arr.append(x)
    err = np.e-x
    err_arr.append(err)

plt.figure(figsize=[4,2.5])
plt.plot(range(1,N+1),np.abs(x_arr),label = r'$(1+1/n)**n$')
plt.axhline(math.e,0,13)

