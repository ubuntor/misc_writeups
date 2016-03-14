# RSA?

Looking at the public key, we have:
```
n = 23292710978670380403641273270002884747060006568046290011918413375473934024039715180540887338067
  = 26440615366395242196516853423447 * 27038194053540661979045656526063 * 32581479300404876772405716877547
e = 3
```

This is multiprime RSA, which is a bit unusual.
The real problem however is that `gcd(e,phi(n)) = 3 != 1`, so our ciphertext is **not** unique!
Instead, let's set `x = inverse_mod(e/3, phi(n)/3)`.
This will give us `c^x = m^(e*x) = m^3 (mod n)`, so we have the cube of the message.

We will need to find all the possible modular cube roots of `m^3` mod each of the three primes, and use CRT to find all the possible messages.
We can do this by implementing the Tonelli-Shanks algorithm extended to cube roots. ([Paper](http://www.sciencedirect.com/science/article/pii/S0893965902000319)) Once we have one cube root, we can multiply by the modular cube roots of unity to find all the other roots.

Code: [rsa.py](rsa.py)

```
Flag: 0ctf{HahA!Thi5_1s_n0T_rSa~}
```
