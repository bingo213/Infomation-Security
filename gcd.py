def gcd(a, b):
    if a < b:
        tmp = a
        a = b
        b = tmp
    while b != 0:
        r = a - int(a/b)*b
        a = b
        b = r
    return a

print(gcd(275481,84923))