import os, sys
#from key import k, random_r
k = 175971776542095822590595405274258668271271366360140578776612582276966567082080372980811310146217399585938214712928761559525614866113821551467842221588432676885027725038849513527080849158072296957428701767142294778752742980766436072183367444762212399986777124093501619273513421803177347181063254421492621011961 # found from break

import msgpack

N = 23927411014020695772934916764953661641310148480977056645255098192491740356525240675906285700516357578929940114553700976167969964364149615226568689224228028461686617293534115788779955597877965044570493457567420874741357186596425753667455266870402154552439899664446413632716747644854897551940777512522044907132864905644212655387223302410896871080751768224091760934209917984213585513510597619708797688705876805464880105797829380326559399723048092175492203894468752718008631464599810632513162129223356467602508095356584405555329096159917957389834381018137378015593755767450675441331998683799788355179363368220408879117131L

def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    g, x, y = egcd(a, m)
    assert g == 1
    return x % m

def pad_even(x):
    return ('', '0')[len(x)%2] + x



def encrypt(ms, k):
    out = [] 
    for i in range(0, len(ms), 256):
        m = ms[i:i+256]
        m = int(m.encode('hex'), 16) # 256 byte chunk of message
        r = random_r()
        r_s = pad_even(format(r, 'x')).decode('hex')
        assert m < N
        c = (pow(k, r, N) * m) % N # m * k**r = c
        c_s = pad_even(format(c, 'x')).decode('hex')
        out.append((r_s, c_s))
    return msgpack.packb(out)

def decrypt(c, k):
    out = ''
    for r_s, c_s in msgpack.unpackb(c):
        r = int(r_s.encode('hex'), 16)
        c = int(c_s.encode('hex'), 16)
        print(r,c)
        k_inv = modinv(k, N)
        out += pad_even(format(pow(k_inv, r, N) * c % N, 'x')).decode('hex')
    return out

def b(m,c): # break: plaintext, ciphertext
    wat = []
    for r_s, c_s in msgpack.unpackb(c):
        r = int(r_s.encode('hex'), 16)
        c = int(c_s.encode('hex'), 16)
        mm = int(m[:256].encode('hex'), 16)
        print(r,hex(mm),hex(c))
        m = m[256:]
        wat.append((r,mm,c))
    print(wat)
    r1,m1,c1 = wat[0]
    r2,m2,c2 = wat[1]
    k1 = (modinv(m1,N)*c1) % N
    k2 = (modinv(m2,N)*c2) % N
    g,x,y = egcd(r1,r2)
    if x < 0:
        k1 = modinv(k1,N)
        x *= -1
    if y < 0:
        k2 = modinv(k2,N)
        y *= -1
    k = (pow(k1,x,N) * pow(k2,y,N)) % N
    print(k)

'''
m * k**r = c

k**r1 = m1^-1 * c1 mod N
k**r2 = m2^-1 * c2 mod N

multiply powers of k**r1 and k**r2 so that you get k
'''

if __name__ == '__main__':
    if sys.argv[1] == 'break': # python special_rsa.py break msg.txt msg.enc
        b(open(sys.argv[2]).read(),open(sys.argv[3]).read())
        sys.exit()

    if len(sys.argv) < 4 or sys.argv[1] not in ('enc', 'dec'):
        print 'usage: %s enc|dec input.file output.file' % sys.argv[0]
        sys.exit()

    with open(sys.argv[3], 'w') as f:
        if sys.argv[1] == 'enc':
            f.write(encrypt(open(sys.argv[2]).read(), k))
        elif sys.argv[1] == 'dec':
            f.write(decrypt(open(sys.argv[2]).read(), k))
