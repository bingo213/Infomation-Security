import math

def primeFactors(n):
    arr = []
    if(n%2==0):
        arr.append(2)
        
    while n % 2 == 0:
        n = n/2

    for i in range(3, int(math.sqrt(n)+1), 2):
        while n%i==0:
            if(len(arr) == 0):
                arr.append(i)
            elif(arr[len(arr)-1] != i):
                arr.append(i)
            n = n/i
    if n > 2:
        arr.append(int(n))
    return arr
        
print(primeFactors(62147910532928227649204848775495221403071692010515734032720947602980996391710))

