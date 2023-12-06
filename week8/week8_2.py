'''
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
    vbar = vy + (-g)*(dt)
    y += dt*(vy+vbar)*0.5

    vy = vbar

    if (y<0.0): break
    t += dt

plt.plot(x_arr,y_arr, "o")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
'''
import numpy as np
import matplotlib.pyplot as plt

g = 9.8
v0 = 10.0
theta = np.pi / 4
maxt = 10.0

dt_values = [0.5,0.2,0.1,0.05,0.02,0.01, 0.005, 0.001]

for dt in dt_values:
    x, y = 0, 0
    t = 0
    vx = v0 * np.cos(theta)
    vy = v0 * np.sin(theta)
    t_arr = []
    x_arr = []
    y_arr = []
    errors = []
    dt_arr = []

    while True:
        t_arr.append(t)
        x_arr.append(x)
        y_arr.append(y)

        x += dt * vx
        vbar = vy + (-g) * (dt)
        y += dt * (vy + vbar) * 0.5
        vy = vbar

        if y < 0.0:
            break
        t += dt
        
        final_x = x_arr[-1]
        expected_x = v0 * np.cos(theta) * t_arr[-1]
        error = abs(final_x - expected_x)
        errors.append(error)
        dt_arr.append(dt)

    print(f'dt = {dt}, Error = {error}')

    plt.plot(x_arr, y_arr,label=f'dt = {dt}')

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
#plt.plot(dt_arr,error)
plt.show()