def gpt(a, b, t):
    if (t%a == 0):
        return int(t/a)
    for i in range (0, b):
        if (b*i+t)%a == 0:
            return int((b*i+t)/a)

#caculate P(x1, y1) + Q(x2, y2)
def addElliptic(a, b, p, x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        # tính (3x1^2 + a) / 2y1 (mod p)
        lamda = gpt((2*y1)%p, p, (3*x1*x1 + a)%p)  
    else: 
        lamda = gpt((x2 - x1)%p, p, (y2 - y1)%p)
    
    x3 = int(lamda*lamda - x1 - x2) % p
    y3 = int(lamda*(x1 - x3) - y1) % p
    return (x3, y3)

# print(addElliptic(2, 2, 17, 6, 3, 5, 1))

#caculate k(x,y)
def doubleAndAdd(a, b, p, k, x, y):
    T = (x, y)
    k0 = []
    while k != 0:
        k0.insert(0, k % 2)
        # k0.append(k%2)
        k = int(k / 2)
    for i in range(1, len(k0)):
        T = addElliptic(a, b, p, T[0], T[1], T[0], T[1])
        if k0[i] == 1:
            T = addElliptic(a, b, p, T[0], T[1], x, y)
    
    return T

print(addElliptic(2, 9, 37897, 32088,18267, 31729, 8298))
# print(doubleAndAdd(2, 9, 37897, 1628, 12111,36058))


