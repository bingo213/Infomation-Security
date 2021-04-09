from gcd import gcd

def f(x):
    return x*x+1

def factor(n, x1):
    x = x1
    x0 = f(x) % n
    p = gcd(abs(x - x0), n)
    i = 1
    while p == 1:
        x = f(x) % n
        x0 = f(x0) % n
        x0 = f(x0) % n
        p = gcd(abs(x - x0), n)
        i += 1

    if p == n:
        return "failure"
    return (p, i)

print(factor(256961, 5000))