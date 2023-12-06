'''
midpoint method
modified euler method
heun method
runge-kutta method order four
'''

from pylab import sin, arange, linspace, plot, show, xlabel, ylabel, title, subplot
#import matplotlib.pyplot as plt

def RK2(f,y0,t,h):
  yi = y0
  yt = []
  for ti in t :
    yt.append(yi)
    k1 = h*f(yi,ti)
    k2 = h*f(yi+0.5*k1,ti+0.5*h)
    yi += k2
  return yt

def RK4(f,y0,t,h):
  yi = y0
  yt = []
  h2 =0.5*h
  for ti in t :
    yt.append(yi)
    k1 = h2*f(yi,ti)
    k2 = h2*f(yi+k1,ti+h2)
    k3 = h*f(yi+k2,ti+h2)
    k4 = h*f(yi+k3,ti+h)
    yi += (2*k1+4*k2+2*k3+k4)/6
  return yt  

def dxdt(x,t):
  return -x**3+sin(t)

a = 0.0
b = 10.0
N = 100
h = (b-a)/N
x0 = 0.0

tpoints = linspace(a,b,N+1)
xpoints = RK2(dxdt,x0,tpoints,h)
x2points = RK4(dxdt,x0,tpoints,h)

subplot(221)
plot(tpoints,xpoints,'r')
xlabel('t')
ylabel('x(t)')
title('RK2')

subplot(222)
plot(tpoints,x2points)
xlabel('t')
ylabel('x(t)')
title('RK4')