# 풀림 방법
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

h = 0.01
MAX = 1000
Error = 1.0E-8

x = np.arange(-1, 1+0.5*h, h)
y = np.arange(-1, 1+0.5*h, h)

X, Y = np.meshgrid(x, y)
Nx, Ny = np.size(x), np.size(y)

phi = np.ones((Nx,Ny)); phi *= 0.1
phi[0,:] = phi[-1,:] = phi[:,-1] = 0.0
phi[Nx//2,Ny//2] = 1.0

for i in range(MAX):
  phi0 = phi.copy()

  for nx in range(1,Nx-1):

    for ny in range(1,Ny-1):
      phi[nx,ny] = (phi0[nx-1,ny]+phi0[nx+1,ny]+phi0[nx,ny-1]+phi0[nx,ny+1])/4.0

  phi[Nx//2,Ny//2] = 1.0

  if np.max(np.abs(phi-phi0)) < Error: break

plt.contour(X,Y,phi.T, levels = np.linspace(np.min(phi), np.max(phi),100))
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar()
plt.show()
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot_surface(X,Y,phi.T)
plt.show()
