import numpy as np 
import matplotlib.pyplot as plt 

g = 9.8
v0 = 10.0
dt = 0.01
theta = np.pi/4
maxt = 10.0
x,y = 0, 0
t = 0
vx = v0*np.cos(theta)
vy = v0*np.sin(theta)
t_arr = []
x_arr = []
y_arr = []

while(True):
    t_arr.append(t)
    x_arr.append(x)
    y_arr.append(y)
    
    x += dt*vx
    vbar = vy + (-g)*dt
    y += dt*(vy+vbar)*0.5

    vy = vbar

    if (y<0.0): break
    t += dt
plt.plot(x_arr,y_arr, "o")
plt.xlabel("x")
plt.ylabel("y")
plt.show()


g = 9.8
v0 = 10.0
dt = 0.01
thetas = np.linspace(0,np.pi/4.0,20,endpoint = True)
theta = np.pi/4
maxt = 10.0
x,y = 0, 0
t = 0
vx = v0*np.cos(theta)
vy = v0*np.sin(theta)
y_arr_s = []
x_arr_s = []
label = []
x_lasts = []

for theta in thetas:
    vx = v0*np.cos(theta)
    vy = v0*np.sin(theta)
    x,y = 0,0
    t_arr = np.arange(0,maxt*dt,dt)
    x_arr = []
    y_arr = []

    for t in t_arr:
        x_arr.append(x)
        y_arr.append(y)
        x += dt*vx

        vy_temp = vy+dt*(-g)
        y += 

for x_arr,y_arrmlabel in zip(x_arr_s, y_arr_s, label_s):
    plt.plot(x_arr,y_arr,label = label)

plt.xlabel("x")
plt.ylabel("y")
plt.show

plt.plot(thetas,x_lasts,'s-')


