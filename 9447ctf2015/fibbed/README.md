# fibbed

The client and server both perform a Diffie-Hellman key exchange, using the
fibonacci numbers modulo some prime `p`. To calculate the order of this group,
we look at the Pisano period. According to the Wikipedia article, since `5` is
not a quadratic residue modulo `p`, the Pisano period divides `p^2-1`. Checking
various factors of `p^2-1` eventually gives us the order:

```
208139237 * 786113149 * 2**2
```

We used the Pohlig-Hellman algorithm to calculate the private key modulo the
factors of the order, by parallelizing it and running it on multiple computers.
We then recovered the private key by CRT, and decrypted the AES-encrypted flag.

Code: [fibbed.py](fibbed.py)
(The commented out parts calculate the private key.)

```
Flag: 9447{Pisan0_mU5t_nEv3r_hAve_THougHt_0f_bruTe_f0rce5}
```
