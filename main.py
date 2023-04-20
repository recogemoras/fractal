import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter):
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    Z = np.zeros_like(C, dtype=int)
    
    for i in range(max_iter):
        mask = np.abs(C) <= 2
        Z[mask] = i
        C[mask] = C[mask] * C[mask] + C[mask]
    
    return Z

if __name__ == "__main__":
    width, height = 1200, 1200
    x_min, x_max = -2, 1
    y_min, y_max = -1, 1
    max_iter = 100

    fractal = mandelbrot_set(width, height, x_min, x_max, y_min, y_max, max_iter)
    plt.imshow(fractal, cmap='PiYG', extent=(x_min, x_max, y_min, y_max))
    plt.show()