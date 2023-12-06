R=15e9
Re=150e9
Ms=2e30
Me=6e24
G=6.67e-11

#Sun
sun=sphere(pos=vector(0,0,0), radius=R, color=color.yellow)
sun.m=Ms

#Earth
earth=sphere(pos=vector(Re,0,0), radius=0.4*R, color=color.green)
earth.m=Me
earth.p=vector(0,30e3,0)*earth.m

sun.p=-(earth.p)

attach_trail(sun)
attach_trail(earth)

t=0
dt=50

while t<15000000000:
    rate(10**5)

    rse=earth.pos-sun.pos

    Fse=-G*sun.m*earth.m*norm(rse)/mag(rse)**2

    Fes=-Fse

    earth.p=earth.p+(Fse)*dt
    sun.p=sun.p+(Fes)*dt
    
    sun.pos=sun.pos+sun.p*dt/sun.m
    earth.pos=earth.pos+earth.p*dt/earth.m
    t=t+dt