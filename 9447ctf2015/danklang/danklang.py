from functools import lru_cache

def binomial(n, k):
    result = 1
    for i in range(1, k+1):
        result = result * (n-i+1) // i
    return result

def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite
 
def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s) 
                   for a in _known_primes[:_precision_for_huge_n])

_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return (fibonacci(n-1) + fibonacci(n-2)) % 987654321

@lru_cache(maxsize=32)
def epicfail(memes):
    wow = 0
    if memes > 1:
        if is_prime(memes):
            wow = bill(memes-1)+1
        else:
            wow = such(memes-1)
    return wow

@lru_cache(maxsize=32)
def such(memes):
    wow = binomial(memes, 5)
    wew = 0
    if wow % 7 == 0:
        wew = bill(memes-1)
        wow += 1
    else:
        wew = epicfail(memes-1)
    wow = wow + wew
    return wow

@lru_cache(maxsize=32)
def bill(memes):
    wew = fibonacci(memes)
    wow = wew
    if wow % 3 == 0:
        wew = such(memes-1)
        wow += 1
    else:
        wew = epicfail(memes-1)
    wow = wow + wew
    return wow

for i in range(1,13379447+1):
    epicfail(i)
    if i % 10000 == 0:
        print(i,epicfail(i))
print(epicfail(13379447))
