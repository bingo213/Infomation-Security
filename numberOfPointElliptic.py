def numberOfPointElliptic(a, b, p):
    Q = {}
    for i in range (1, int((p-1)/2) +1):
        Q[(i*i) % p] = i
    count = 0
    for x in range (0, p):
        r = (x*x*x + a * x + b) % p
        if r in Q:
            count += 2
            print (x, Q[r])
            print (x, p - Q[r])
    return count + 1

print(numberOfPointElliptic(5, 6, 43))

# def isPrime(n):
#     # Corner case
#     if (n <= 1):
#         return False

#     # Check from 2 to n-1
#     for i in range(2, n):
#         if (n % i == 0):
#             return False

#     return True
    
# p = 47339
# for i in range(1, 30):
#     for j in range(1, 30):
#         number = numberOfPointElliptic(i,j, p)
#         if(isPrime(number)):
#             print (i, j, number)

#             break