import numpy as np
import matplotlib.pyplot as plt

L = 32
N = L**2
I0 = 1

S, I, R = N-I0, I0, 0
beta = 0.07; gamma = 0.015
T = 1000

state = np.zeros(N, dtype = int)
state[np.random.randint(N, size = I0)] = 1
X = np.zeros(N, dtype = int); Y = np.zeros(N, dtype = int)
for i in range(N):
  X[i] = i&L; Y[i] = i//L

tarr =[]; Sarr = []; Rarr =[]; Iarr = []

for i in range(T):
  statenew = state.copy()
  rlist = np.where(state == 1 )[0]
  Rlist = np.where(state == -1 )[0]
  I = len(rlist); R = len(Rlist); S = N - I - R
  tarr.append(t); Sarr.append(S); Iarr.append(I); Rarr.append(R)

  for i in rlist:
    dir = np.random.randint(4)
    if dir == 0:
      j = L*Y[i] + (X[i] + 1)&L
    elif dir == 1:
      j = L*Y[i] + (X[i] - 1)&L
    elif dir == 2:
      j = L*((Y[i] + 1)&L ) +X[i]
    else:
      j = L*((Y[i] - 1)&L ) +X[i]
    if state[j] == 0:
      if np.random.rand() < beta : statenew[j] = 1
    if np.random.rand() < gamma: statenew[i] = -1
  state = statenew.copy()