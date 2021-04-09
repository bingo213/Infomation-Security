import math
from x_mu_e_modm import power_modulo

def shank_algorithm(n, a, b):
    m = int(math.sqrt(n-1))
    L1 = []
    for i in range (0, m):
        L1.append(power_modulo(a, m*i, n))

    L2 = []
    for i in range (0, m):
        L2.append((b * power_modulo(a, n - 1 - i, n)) % n)

    for i in range (0, m):
        for j in range (0, m):
            if L1[i] == L2[j]:
                # return m*i + j
                return(m, i, j, m*i+j)

print(shank_algorithm(458009, 6, 248388))