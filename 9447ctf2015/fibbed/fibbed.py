import sys

p = 981725946171163877
serverkey = (58449491987662952,704965025359609904)
clientkey = (453665378628814896,152333692332446539)
g = (0,1)

def mult(m1, m2, p):
    r = [[0,0], [0,0]]
    for i in range(2):
        for j in range(2):
            t = 0
            for k in range(2):
                t += m1[i][k] * m2[k][j]
            r[i][j] = t % p
    return r

def calcM(p, l, base):
    if l == 0:
        return [[base[1], base[0]], [base[0], base[1]]]
    x1 = [[base[0], base[1]], [base[1], (base[0] + base[1]) % p]]
    x2 = mult(x1, x1, p)
    for i in bin(l)[3:]:
        if i == '1':
            x1 = mult(x1, x2, p)
            x2 = mult(x2, x2, p)
        else:
            x2 = mult(x1, x2, p)
            x1 = mult(x1, x1, p)
    return x1

def calcM2(a,base,p):
    x = [[g[1], g[0]], [g[0], g[1]]]
    xx = [[base[0], base[1]], [base[1], (base[0] + base[1]) % p]]
    bits = "{0:b}".format(a)
    for i, bit in enumerate(bits):
        if bit=='1': x = mult(mult(x,x,p),xx,p)
        elif bit=='0': x = mult(x,x,p)
    return x[0]

period = 208139237 * 786113149 * 2**2
p1 = 208139237
p2 = 786113149

'''
limit = int(sys.argv[1])

key1 = calcM(p1*4,g,p)
check1 = calcM(p1*4,serverkey,p)

for i in range(limit,p2):
    if i % 10000 == 0:
        print(i)
    if calcM2(i,key1,p) == check1:
        print("found i:",i)
        break
'''
pm1 = 159461786
'''
limit = int(sys.argv[1])

key1 = calcM(p2*4,g,p)
check1 = calcM(p2*4,serverkey,p)

for i in range(limit,p1):
    if i % 10000 == 0:
        print(i)
    if calcM2(i,key1,p) == check1:
        print("found i:",i)
        break
'''
pm2 = 651752996


print("done")
import socket
import sys
from Crypto.Cipher import AES
import binascii
import hashlib
IV = "0123456789ABCDEF"
message = '59719af4dbb78be07d0398711c0607916dd59bfa57b297cd220b9d2d7d217f278db6adca88c9802098ba704a18cce7dd0124f8ce492b39b64ced0843862ac2a6'

def decrypt(text, passphrase):
	key = hashlib.sha256(passphrase).digest()
	aes = AES.new(key, AES.MODE_CBC, IV)
	return aes.decrypt(binascii.unhexlify(text))

from sage.all import *
for i in range(4):
    s = crt([pm1,pm2,i],[p1,p2,4])
    print(i, s)
    print(calcM(p,s,clientkey))
    key = str(calcM(p,s,clientkey))
    print(decrypt(message,key))
