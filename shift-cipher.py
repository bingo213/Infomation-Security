def shif_cipher(s, key):
    decryption = ""
    for i in s:
        tmp = ord(i)-key-ord('a')
        # print(tmp)
        decryption += chr(tmp%26+ord('a'))
    return decryption

# for i in range (1, 26):
#     print("key = " + str(i) + ": " + shif_cipher("beeakfydjxuqyhyjiqryhtyjiqfbqduyjiikfuhcqd", i))

def count_character(s, acii_code):
    count = 0
    for i in s:
        if ord(i) == acii_code:
            count += 1
    return count

s = "KQEREJEBCPPCJCRKIEACUZBKRVPKRBCIBQCARBJCVFCUPKRIOFKPACUZQEPBKRXPEIIEABDKPBCPFCDCCAFIEABDKPBCPFEQPKAZBKRHAIBKAPCCIBURCCDKDCCJCIDFUIXPAFFERBICZDFKABICBBENEFCUPJCVKABPCYDCCDPKBCOCPERKIVKSCPICBRKIJPKABI"
for i in range (65, 91):
    print(chr(i) + ": " + str(count_character(s, i)))