import numpy as np
import matplotlib.pyplot as plt

N = 10000
sum = 0.0
x_arr = []
sum_arr =[]
err_arr = []
n_s=[]

for n in range(N):
    x=(-1)**n/(2*n+1)
    x_arr.append(x)
    sum += x
    sum_arr.append(sum*4)
    err_arr.append(4*sum-np.pi)
    #if n%100 ==0:
        #print(n, 4*sum) 

plt.plot(range(N),x_arr)
plt.plot(range(N),np.abs(err_arr))
plt.xscale('log')
plt.grid()
plt.loglog()
# log*log => 기울기가 -1인 이유 : 1/n씩 정확해지니까 log(1/n)-> n**(-1) 따라서 수렴해간다는 의미

N = 10000
sum = 0.0
n=0
for n in range(N):
    x=1/(n**2)
    sum += x   
    print(n,sum)

N = 10000
eps = 1e-3
sum = 0.0
n=0
'''
while n < N :
    x=(-1)**n/(2*n+1)
    sum += x   
    if (abs(x)<eps): break
    if(n%100==0):
        print(n,4*sum)
    n += 1
'''
while(True):
    x=(-1)**n/(2*n+1)
    sum += x   
    if (abs(x)<eps): break
    if(n%100==0):
        print(n,4*sum)
    n += 1
    
# a==b, a!=b, a||b, a&&b
# 같다, 같지않다, or,  and
