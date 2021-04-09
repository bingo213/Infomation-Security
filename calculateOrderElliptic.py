def gpt(a, b, t):
    for i in range (0, b):
        if (b*i+t)%a == 0:
            return (b*i+t)/a

# Tinh bac cua diem (x,y) tren duong cong Elliptic co pt:
# y^2 = (x  ^3 + ax + b) modp
# biet co n diem
def calOrder(a, b, p, n, x, y):
    lamda = gpt((2*y)%p, p, (3*x*x + a)%p)
    x3 = (lamda*lamda-2*x)%p
    y3 = lamda*(x - x3) -y
    T = (x3, y3)

    for i in range (3, n+1):
        if x == T[0]:
            return i
        lamda = gpt((x-T[0])%p, p, (y - T[1])%p)
        x3 = (lamda*lamda-T[0]-x)%p
        y3 = lamda*(T[0] - x3) -T[1]
        T = (x3, y3)


print(calOrder(2, 5, 43, 45, 36, 11))