def ExpBin(M,e,n):
    e_bin = bin(e)[2:]
    #print("e en binario:", e_bin)
    if e_bin[0] == '1': C = M
    else: C = 1
    for i in range(1, len(e_bin)):
        C = (C * C) % n
        if e_bin[i] == '1': C = (C * M) % n
    return C

import sys
a, b, c = map(int, sys.stdin.read().split())
print(ExpBin(a, b, c))

#print(ExpBin(3,381,10))
#print(ExpBin(3,34505,100)) # 3^34505 mod 100 = 43
#print(ExpBin(2,342405,101)) # 2^342405 mod 101 = 32
#print(ExpBin(7,32945718283912847,26)) # 7^32945718283912847 mod 26 = 7
#print(ExpBin(2,1234,789)) # 2^1234 mod 789 = 481