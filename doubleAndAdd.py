# def gpt(a, b, t):
#     if (t%a == 0):
#         return int(t/a)
#     for i in range (0, b):
#         if (b*i+t)%a == 0:
#             return int((b*i+t)/a)

# #caculate P(x1, y1) + Q(x2, y2)
# def addElliptic(a, b, p, x1, y1, x2, y2):
#     if x1 == x2 and y1 == y2:
#         # tính (3x1^2 + a) / 2y1 (mod p)
#         lamda = gpt((2*y1)%p, p, (3*x1*x1 + a)%p)  
#     else: 
#         lamda = gpt((x2 - x1)%p, p, (y2 - y1)%p)
    
#     x3 = int(lamda*lamda - x1 - x2) % p
#     y3 = int(lamda*(x1 - x3) - y1) % p
#     return (x3, y3)

# # print(addElliptic(2, 2, 17, 6, 3, 5, 1))

# #caculate k(x,y)
# def doubleAndAdd(a, b, p, k, x, y):
#     T = (x, y)
#     k0 = []
#     while k != 0:
#         k0.insert(0, k % 2)
#         # k0.append(k%2)
#         k = int(k / 2)
#     for i in range(1, len(k0)):
#         T = addElliptic(a, b, p, T[0], T[1], T[0], T[1])
#         if k0[i] == 1:
#             T = addElliptic(a, b, p, T[0], T[1], x, y)
    
#     return T

# # print(addElliptic(2, 9, 37897, 32088,18267, 31729, 8298))
# print(doubleAndAdd(2, 6, 66586029242214827589815435761546197628406466426497, 3, 1,3))


def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)
# calculate `modular inverse`
def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m

# double function
def ecc_double(x1, y1, p, a):
    s = ((3*(x1**2) + a) * modinv(2*y1, p))%p
    x3 = (s**2 - x1 - x1)%p
    y3 = (s*(x1-x3) - y1)%p
    return (x3, y3)
# add function
def ecc_add(x1, y1, x2, y2, p, a):
    s = 0
    if (x1==x2):
        s = ((3*(x1**2) + a) * modinv(2*y1, p))%p
    else:
        s = ((y2-y1) * modinv(x2-x1, p))%p
    x3 = (s**2 - x1 - x2)%p
    y3 = (s*(x1 - x3) - y1)%p
    return (x3, y3)
def double_and_add(multi, generator, p, a):
    (x3, y3)=(0, 0)
    (x1, y1) = generator
    (x_tmp, y_tmp) = generator
    init = 0
    for i in str(bin(multi)[2:]):
        if (i=='1') and (init==0):
            init = 1
        elif (i=='1') and (init==1):
            (x3,y3) = ecc_double(x_tmp, y_tmp, p, a)
            (x3,y3) = ecc_add(x1, y1, x3, y3, p, a)
            (x_tmp, y_tmp) = (x3, y3)
        else:
            (x3, y3) = ecc_double(x_tmp, y_tmp, p, a)
            (x_tmp, y_tmp) = (x3, y3)
    return (x3, y3)