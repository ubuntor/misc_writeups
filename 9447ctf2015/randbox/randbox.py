from pwn import *
import string

r = remote('randBox-iw8w3ae3.9447.plumbing',9447)

al = "0123456789abcdef"

def ind(c):
    return al.index(c)

def tr(c,f,t):
    return c.translate(string.maketrans(f,t))

def h(i):
    return hex(i%16)[-1]

print r.recvline()

log.info('round 1')
target = r.recvline().split('\'')[1]
r.recvline()
r.sendline(al)
key = r.recvline().strip()
r.recvline()
out = tr(target,key,al)
#print(target,key,al,out)
r.sendline(out)
print `r.recvline()`
print `r.recvline()`

log.info('round 2')
target = r.recvline().split('\'')[1]
r.recvline()
r.sendline("1"+"0"*31)
key = r.recvline().strip()
r.recvline()
indd = key.index('1')
out = target[indd:] + target[:indd]
#print(target,key,al,out)
r.sendline(out)
print `r.recvline()`
print `r.recvline()`

log.info('round 3')
target = r.recvline().split('\'')[1]
r.recvline()
r.sendline(target)
key = r.recvline().strip()
r.recvline()
out = key
#print(target,key,al,out)
r.sendline(out)
print `r.recvline()`
print `r.recvline()`

log.info('round 4')
target = r.recvline().split('\'')[1]
r.recvline()
r.sendline(al)
key = r.recvline().strip()
r.recvline()
out = tr(target,key,al)
#print(target,key,al,out)
r.sendline(out)
print `r.recvline()`
print `r.recvline()`

log.info('round 5')
target = r.recvline().split('\'')[1]
r.recvline()
r.sendline(target)
key = r.recvline().strip()
r.recvline()
out = key
#print(target,key,al,out)
r.sendline(out)
print `r.recvline()`
print `r.recvline()`

log.info('round 6')
target = r.recvline().split('\'')[1]
r.recvline()
r.sendline(target)
out = r.recvline().strip()
r.recvline()
#print(target,out)
key = [(ind(target[i]) - ind(out[i]))%16 for i in range(32)]
final = ''.join(al[(ind(target[i])+key[i])%16] for i in range(32))
#print(final)
r.sendline(final)
print `r.recvline()`
print `r.recvline()`

r.recvline()

log.info('round 7')
target = r.recvline().split('\'')[1]
r.recvline()
inn = '0'
r.sendline(inn)
out = r.recvline().strip()
r.recvline()
#print(inn,out)
iv = int(out,16)
final = ''
for i in range(len(target)):
    if i == 0:
        final = h(iv^int(target[0],16))
    else:
        final += h(int(final[i-1],16)^int(target[i],16))
#print(target,final)
r.sendline(final)
print `r.recvline()`
print `r.recvline()`

log.info('round 8')
target = r.recvline().split('\'')[1]
r.recvline()
inn = '0'
r.sendline(inn)
out = r.recvline().strip()
r.recvline()
#print(inn,out)
iv = int(out,16)
final = ''
for i in range(len(target)):
    if i == 0:
        final = h(int(target[0],16)-iv)
    else:
        final += h(int(target[i],16)-int(target[i-1],16))
#print(target,final)
r.sendline(final)
print `r.recvline()`
print `r.recvline()`

log.info('round 9')
target = r.recvline().split('\'')[1]
r.recvline()
inn = '0'
r.sendline(inn)
out = r.recvline().strip()
r.recvline()
#print(inn,out)
iv = int(out,16)
final = ''
for i in range(len(target)):
    if i == 0:
        final = h(iv^int(target[0],16))
    else:
        final += h(int(final[i-1],16)^int(target[i],16))
#print(target,final)
r.sendline(final)
print `r.recvline()`
print `r.recvline()`

log.info('round 10')
target = r.recvline().split('\'')[1]
r.recvline()
inn = '00'
r.sendline(inn)
out = r.recvline().strip()
r.recvline()
print(inn,out)
xor = int(out,16) % 0x10
final = ''.join(h(xor^int(target[i^1],16)) for i in range(len(target)))
print(target,final)
r.sendline(final)
print `r.recvline()`
print `r.recvline()`

print `r.recvline()`
print `r.recvline()`
print `r.recvline()`
print `r.recvline()`
print `r.recvline()`
