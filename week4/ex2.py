import numpy as np
import matplotlib.pyplot as plt

image = 1024
conv = 10e-3
max_iter = 40
h = 10e-4

x_min = -1.0
x_max = 1.0
y_min = -1.0
y_max = 1.0

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255),
          (255, 255, 0), (255, 0, 255), (0, 255, 255)]

def convert_coords(x, y):
    z_y = y * (y_max - y_min) / (image - 1) + y_min
    z_x = x * (x_max - x_min) / (image - 1) + x_min
    return complex(z_x, z_y)

def find_root(f, z, err, iterCount):
    tmp = z + err + 1
    iteration = 0
    while (abs(tmp - z) > err) and (iteration < iterCount):
        fz = f(z)
        df_dz = (f(z + complex(h, h)) - fz) / complex(h, h)
        if df_dz == 0:
            return None
        tmp = z
        z = z - fz / df_dz
        iteration += 1
    return (z, iteration)

def get_root_number(z, roots):
    minDistance = abs(z - roots[0])
    rootNumber = 0
    for k in range(1, len(roots)):
        tmp = abs(z - roots[k])
        if tmp < minDistance:
            minDistance = tmp
            rootNumber = k
    return rootNumber


def draw_fractal(fun, roots):
    fractal = np.zeros((image, image, 3), dtype=np.uint8)

    for x in range(image):
        for y in range(image):
            res = find_root(fun, convert_coords(x, y), conv, max_iter)
            if res is None:
                continue
            z, i = res
            rootColor = colors[get_root_number(z, roots)]
            depth = (max_iter - i) / max_iter
            RGB = [int(depth * a) for a in rootColor]
            fractal[y, x] = RGB

    plt.imshow(fractal)
    plt.show()

def f1(z):
    return z ** 3 - 1

f1_roots = ( np.exp(4j * np.pi / 3),np.exp(2j * np.pi / 3), 1)

draw_fractal(f1, f1_roots)
