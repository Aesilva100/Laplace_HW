
import numpy as np
import matplotlib.pyplot as plt
from laplace_solver import laplace_solver

# Definición de las condiciones de frontera
N = 10
M = 10
V0 = np.zeros((N, M))
V0[:, 0] = -2  # Borde izquierdo
V0[:, -1] = 2  # Borde derecho
V0[0, :] = 0   # Borde superior
V0[-1, :] = 0  # Borde inferior

# Resolución de la ecuación de Laplace
V = laplace_solver(N, M, V0)

# Visualización de la solución
plt.imshow(V, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Solución numérica de la ecuación de Laplace')
plt.show()
