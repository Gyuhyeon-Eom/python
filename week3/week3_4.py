from vpython import*
'''
scene.background = color.gray(1)
s = sphere(pos=vec(1,0,0), radius=0.1, color=color.cyan)
'''

for i in range(314):
    rate(10)
    theta = pi*0.1*i
    x = cos(theta)
    y = sin(theta)
    s.pos = vec(x,y,0)