# People's Square

Reversing the binary, we have a guessing game that uses 4-round AES encryption. There are 1024 pairs of ciphertexts with plaintexts of the following form:
```
(8 bytes of 0x00 or 0x01) || (the current count [4 bytes]) || (a time [4 bytes])
```

Since we can group these into sets of 256 plaintexts with only one byte changing (the bytes of the count), we can use the Square attack on 4-round AES to recover the last round's key, and invert that through the key scheduling rounds to get the original key, and decrypt the flag.

Code: [break.py](break.py)

```
Flag: 0CTF{~R0MAN_l0VES_B10CK_C1PHER~}
```
