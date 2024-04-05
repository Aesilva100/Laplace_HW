
import numpy as np

def laplace_solver(N, M, V0, tolerancia=1e-4, max_iteraciones=1000):
    '''
    Resuelve la ecuación de Laplace para una red de puntos 2D usando el método de relajación.

    Parámetros:
    N, M : int
        Número de puntos en las direcciones x e y de la red.
    V0 : ndarray
        Matriz de NxM que representa los valores de frontera para V(x, y).
    tolerancia : float
        Tolerancia para la convergencia del método.
    max_iteraciones : int
        Número máximo de iteraciones.

    Retorna:
    V : ndarray
        Matriz de NxM con la solución numérica de V(x, y).
    '''
    V = np.zeros((N, M))
    V[:, 0] = V0[:, 0]
    V[:, -1] = V0[:, -1]
    V[0, :] = V0[0, :]
    V[-1, :] = V0[-1, :]

    iteraciones = 0
    while iteraciones < max_iteraciones:
        V_old = np.copy(V)
        for i in range(1, N-1):
            for j in range(1, M-1):
                V[i, j] = 0.25 * (V_old[i+1, j] + V_old[i-1, j] + V_old[i, j+1] + V_old[i, j-1])

        if np.max(np.abs(V - V_old)) < tolerancia:
            break

        iteraciones += 1

    return V
