import numpy as np

import random as rand

from moda import Moda

def inicializar(cant):
    arreglo = np.empty(cant, dtype=int)
    for i in range(cant):
        arreglo[i] = rand.randint(0, cant//2)
    return arreglo
if __name__ == '__main__':
    cant = int(input('Ingrese la cantidad: '))
    vector = inicializar(cant)
    moda = Moda()
    print('Vector', vector)
    print('Moda del vector:', moda.calcular(vector))