def power_modulo(x, e, m):
    power = x
    a = 1
    ei = e % 2
    while(e >= 1):
        if ei == 1:
            a = (a * power) % m
            
        e = int(e/2)
        ei = e % 2
        power = (power * power) % m
    return a

# print(power_modulo(69701, 28135, 28657))