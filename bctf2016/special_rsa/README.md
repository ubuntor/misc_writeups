# Special RSA

Looking at the code, `encrypt` takes a message, breaks it up into 256 byte chunks, and for each one, multiplies it by `k^r` for a random `r`, then stores the ciphertext and `r`, all mod `N`.

We're given `msg.txt` and `msg.enc`, which have has two chunks, giving us two plaintext-ciphertext pairs.
Now, `m * k^r = c mod N`, so `k^r = m^-1 * c mod N`. We have two pairs, giving us:
```
k^r1 = m1^-1 * c1 mod N
k^r2 = m2^-1 * c2 mod N
```

Since `gcd(r1,r2) = 1`, we can use the extended Euclidean algorithm to find some `a` and `b` such that `a*r1 + b*r2 = 1`. Then, `(k^r1)^a * (k^r2)^b = k`, so we can recover `k`, and decrypt the flag.

Code: [special_rsa.py](special_rsa.py)
