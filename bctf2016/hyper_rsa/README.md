# Hyper RSA

Looking at the code, it essentially uses RSA 2 times. We can recover `p1`, `q1`, `p2`, and `q2` from the server by getting `e` and `d` pairs for both moduli, and using https://gist.github.com/ddddavidee/b34c2b67757a54ce75cb.

We're given a plaintext-ciphertext pair, and we're asked to decrypt another ciphertext.
Running strings on `hyper_rsa.jpg` gives us `m1`, `c1`, and `c2` without having to use OCR. (how thoughtful!)

We used a meet-in-the-middle attack to recover `e1` and `e2`, by encrypting `m1` with all possible `e1`, storing the results in a hashtable, and decrypting `c1` with all possible `d2` (calculated from `e2` and `phi2 = (p2-1)*(q2-1)`) to find a match. `e1` and `e2` need to be relatively prime to `phi1` and `phi2`, ruling out all even `e1` and `e2`. To save memory, we only store the last 64 bits of the encrypted `m1`. (The birthday problem wasn't an issue with the number of possible `e1`).

We implemented this in C++ with GMP for bignums and OpenMP for speed. (The first half isn't parallelized since `unordered_map` isn't thread-safe for multiple writes.) After running for a really long time, this gave us `e1` and `e2`, which we could use to decrypt `c2`.

Code: [hyper_rsa.cpp](hyper_rsa.cpp)
