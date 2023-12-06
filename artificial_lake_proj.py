# 비압축성, roe = constant, 비회전, 소용돌이도 x
# ∂η/∂t + ∂Φ /∂x*(∂η/∂x) = ∂Φ/∂z, at z = η(x,t);
# η:표면 고도
# (∂Φ/∂z)*(∂s/∂z)+(∂s/∂t)=∂Φ/∂x, at x=s(z,t).
# ∂^2Φ/∂x^2 + ∂^2Φ/∂z^2 = 0, -h<=z<=0
# ∂Φ/Φz = 0 , at z = -h
# ∂η/Φt = ∂Φ/Φz , at z = 0
# η + 1/g*(∂Φ/Φt) = 0 , at z = 0
# ∂Φ/Φx = ∂s(z,t)/Φt, at x = 0
# s(z,t) = 1/2*S(z)sin(ωt + ψ) 
# s(z,t) = 1/2*S(1+z/d)sin(ωt + ψ) , -d<=z<=0
# s(z,t) = 0, -h<=z<=-d
# ω^2 = gktanhkh
# σ&2/kh = tanhkh
# Φ(x,z,t) = g/ω[ A* (cosh k(h+z)/coshkh)* sin(kx−ωt−ψ) +g/ω[C*exp(-kx)* (cosh k(h+z)/coshkh)* cos(ωt+ψ) 
# A = 2*(sinh kh/ kd)*(cosh k(h-d)+kdsinh kh - coshkh)/(skh+sinh2kh) * S
# A is the progressive amplitude and H = 2A is the wave height
# η= H/2 * cos(kx−ωt−ψ), κx≫1.
# When the hinge of the flap is located at the 
# bottom of the wave tank we have d = h and the ratio becomes
# (H/S) = 4*(sinhkh/kh)*(1+khsinhkh - coshkh)/(2kh + sinh2kh)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

T = float(input("파도의 주기를 입력하세요: "))
h = float(input("인공호수의 수심을 입력하세요: "))
x0 = 0.0001 #초기 파고
g = 9.81
length = 50 #에리카 인공호수의 길이
#진폭을 정하더라도, 인공호수 진폭을 설정하기

if np.sign(h) == -1:
    h = -h

# Newton-Rapshon
omega_2 = ((2 * np.pi) / T) ** 2
Gamma = (omega_2 * h) / 9.81

con = 1
x = np.zeros(100)  # 충분히 큰 배열로 초기화

if x0 != 0:
    x[con] = x0
    x[con + 1] = x[con] - ((Gamma - (x[con] * np.tanh(x[con]))) /
                           ((-x[con] * (1 / np.cosh(x[con])) ** 2) - np.tanh(x[con])))
    while abs(x[con + 1] - x[con]) > 0.00001:
        x[con + 2] = x[con + 1] - ((Gamma - (x[con + 1] * np.tanh(x[con + 1]))) /
                                    ((-x[con + 1] * (1 / np.cosh(x[con + 1])) ** 2) - np.tanh(x[con + 1])))
        con += 1

kr = x[con] / h
Lr = (2 * np.pi) / kr
omega = np.sqrt(omega_2)
Cr = Lr / T
nr = 0.5 * (1 + ((2 * kr * h) / np.sinh(2 * kr * h)))
Cgr = nr * Cr

x = np.linspace(0, length, 500)

print('    Method:         L(m):     k(1/m):   omega(1/T):     C(m/s):   n:       Cg(m/s):   error*100')
print('---------------------------------------------------------------------------------------------')
print(f'Newton-Raphson:     {Lr:.3f}   {kr:.3f}      {omega:.3f}        {Cr:.3f}    {nr:.3f}   {Cgr:.3f}      -')

def calculate_amplitude(T, h):

    kh = np.sqrt((2 * np.pi / T) ** 2 * h * g)
    A = 4 * (np.sinh(kh) / kh) * (1 + kh * np.sinh(kh) - np.cosh(kh)) / (2 * kh + np.sinh(2 * kh))
    print(A) #진폭

    return A

def artificial_lake_proj(T, h):

    A = calculate_amplitude(T, h)
    timesteps = 100
    x = np.linspace(0, length, 500)
    times = np.linspace(0, 10, timesteps)

    fig, ax = plt.subplots()
    line, = ax.plot([], [], lw=2)
    ax.set_xlim(0, length)
    ax.set_ylim(-1.5 * A, 1.5 * A)  # 진폭 범위
    ax.set_xlabel("Distance")
    ax.set_ylabel("Amplitude")
    ax.set_title("Regular Wave Animation")

    def init():
        line.set_data([], [])
        return line,

    def update(frame):
        time = frame / 100
        wave = A * np.cos(2 * np.pi * (x - time * Cr) / Lr)  # 주기와 속력을 고려한 코사인 함수 사용

        line.set_data(x, wave)
        return line,


    ani = FuncAnimation(fig, update, frames=timesteps, init_func=init, blit=True, interval=50)
    plt.show()

artificial_lake_proj(T, h)



h_desired = 1.6
target = 1e-4
max_iterations = 1000

def find_period(desired_height, target_height, tol, max_iter):
    a, b = 0.1, 10.0
    iterations = 0\
    
    while iterations < max_iter:
        T = (a + b) / 2
        calculated_height = calculate_amplitude(T, h_desired)

        if abs(calculated_height - desired_height) < tol:
            return T, calculated_height

        if calculated_height < desired_height:
            a = T
        else:
            b = T

        iterations += 1

    return None, None

found_period, wave_height = find_period(h_desired, target, target, max_iterations)

if found_period is not None:

    print(f"원하는 파고에 대한 주기: {found_period} s")
    
else:
    print("원하는 파고에 대한 주기를 찾지 못했습니다.")



