def power_modulo(x,e,m):
    if m == 1:
        return 0
    r = 1
    x = x % m
    while e > 0:
        if(e % 2 ==1):
            r = (r*x)%m
        e = e >> 1
        x = (x*x)%m
    return r

# print(power_modulo(69701, 28135, 28657))