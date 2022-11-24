import numpy as np
from numpy import float64

if __name__ == '__main__':
    R = float64(input("Digite o raio R da circunferência: "))
    n = int(input("Digite o número de iterações que deseja: "))
    ln = float64(np.sqrt(2))
    soma = ln
    x = 4
    for i in range(n):
        print(ln)
        ln = float64(np.sqrt(R * (2 * R - np.sqrt(4 * R * R - ln * ln))))
        soma += ln
        x = x * 2

    print(f"L{x} = {soma}")
