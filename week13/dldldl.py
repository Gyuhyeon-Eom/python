import numpy as np
import matplotlib.pyplot as plt

length = 10
timesteps = 1000
flap_frequency = 0.5
flap_amplitude = 1.0

T = float(input("파도의 주기를 입력하세요: "))
h = 10
x0 = 0.0001

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


for i in range(timesteps):
    time = i / 100

    flap_position = flap_amplitude * np.sin(2 * np.pi * flap_frequency * time)
    wave = np.sin(2 * np.pi * (x - Cr * time - flap_position) / length)

    plt.clf()
    plt.plot(x, wave, color='blue')
    plt.title(f"Wave Animation at t = {time:.2f} seconds")
    plt.xlabel("Distance")
    plt.ylabel("Amplitude")
    plt.ylim(-1.5, 1.5)
    plt.grid(True)
    plt.pause(0.05)

plt.show()
