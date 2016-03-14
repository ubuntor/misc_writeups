from sage.all import *
import binascii
import base64
import math
from Crypto.PublicKey import RSA

def cuberoot(a, p):
    if p == 2:
        return a
    if p == 3:
        return a
    if (p%3) == 2:
        return pow(a,(2*p - 1)/3, p)
    if (p%9) == 4:
        root = pow(a,(2*p + 1)/9, p)
        if pow(root,3,p) == a%p:
            return root
        else:
            return None
    if (p%9) == 7:
        root = pow(a,(p + 2)/9, p)
        if pow(root,3,p) == a%p:
            return root
        else:
            return None
    else:
        # tonelli-shanks extension to cube roots (http://www.sciencedirect.com/science/article/pii/S0893965902000319)
        # it's incomplete, but w/e, it works
        e = 2 # power of 3 in p-1
        q = (p-1)/(3**e)
        Z = Zmod(p)
        while True:
            h = Z.random_element()
            # check if cubic nonresidue?
            g = h**q
            symbol = -1 # ???
            y = g
            r = e
            b = 0
            if q%3 == 2:
                x = a**((q-2)/3)
            else:
                x = a**((2*q-2)/3)
                b = a**2 * x**3
                x = a*x
            if b%p == 1:
                return x
        return 0

# the modulus that we were given
N = long(23292710978670380403641273270002884747060006568046290011918413375473934024039715180540887338067)
# we have fricking 3 primes wth
p1 = 26440615366395242196516853423447
p2 = 27038194053540661979045656526063
p3 = 32581479300404876772405716877547
e = long(3)

print "p1 stuff:",gcd(e,p1-1),p1%3,p1%9 # argh
print "p2 stuff:",gcd(e,p2-1),p2%3,p2%9
print "p3 stuff:",gcd(e,p3-1),p3%3,p3%9

print "flying?", (p1*p2*p3 == N)

eulerphi = (p1-1)*(p2-1)*(p3-1)

print "phi(n)", eulerphi
print "----"
print "gcd:",gcd(e, eulerphi)
x = inverse_mod(e/3, eulerphi/3)

print "x:",x

c = int(binascii.hexlify(base64.b64decode("AExBYqB6ARG4NExosRi9BUrLw4wxMbaomZyR0bPi2C3Hw6HhA0/WBA==")),16)
print "c:",c

# c**x = m**(e*x) = m**3
m3 = pow(c,x,N)
print "m^3:",m3

m31 = mod(m3,p1)
m32 = mod(m3,p2)
m33 = mod(m3,p3) 
#print m31,m32,m33

r1 = cuberoot(m31,p1)
r2 = cuberoot(m32,p2)
r3 = cuberoot(m33,p3)
print r1, r2, r3

cr1 = [r1 * i for i in [1]+Zmod(p1).zeta(3,all=True)]
cr2 = [r2 * i for i in [1]+Zmod(p2).zeta(3,all=True)]
cr3 = [r3 * i for i in [1]+Zmod(p3).zeta(3,all=True)]
print cr1,cr2,cr3

# should all be zeroes
cr1t = [(r1 * i)**3 - m31 for i in [1]+Zmod(p1).zeta(3,all=True)]
cr2t = [(r2 * i)**3 - m32 for i in [1]+Zmod(p2).zeta(3,all=True)]
cr3t = [(r3 * i)**3 - m33 for i in [1]+Zmod(p3).zeta(3,all=True)]
print cr1t,cr2t,cr3t

for r1 in cr1:
    for r2 in cr2:
        for r3 in cr3:
            m = crt([int(r1),int(r2),int(r3)], [p1,p2,p3])
            x = '%x' % (m,)
            h = ('0' * (len(x) % 2)) + x
            hh = h.decode('hex')
            if '0ctf' in hh:
                print hh
