from x_mu_e_modm import power_modulo

def find_primitive_element(p):
    i = 2
    j = 0
    e = []
    n = p-1

    while(i<=n):
        if n%i==0:
            if i!=j:
                e.append(i)
                j = i
            n = n/i
        else:
            if i%2==0:
                i += 1
            else:
                i += 2
    
    tmp = 0
    for x in range (2, p):
        tmp = 0
        for ei in e:
            if power_modulo(x, ei, p) != 1:
                tmp += 1
            else:
                break
        if tmp == len(e):
            return x

# def ElGamal_encryption(x, p, alpha, beta, k):
#     return (power_modulo(alpha, k, p), (x * power_modulo(beta, k, p)) % p)

# def ElGamal_decryption(encryp, a, p):
#     return (encryp[1] * power_modulo(encryp[0], p-a-1, p)) % p

# def main():
#     p = 4334944379
#     alpha = find_primitive_element(p)
#     a = 521
#     beta = power_modulo(alpha, a, p)
#     x = 128557
#     k = 1003

#     ek = ElGamal_encryption(x, p, alpha, beta, k)

#     print("e(k) = " + str(ek))
#     print("d(k) = " + str(ElGamal_decryption(ek, a, p)))

# main()

print(find_primitive_element(489133282872437279))


