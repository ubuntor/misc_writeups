# zerodaystore

We decompiled the given apk to find where the server was running.
We could order and pay for items manually, but all the items had a price greater than 0.
We needed to somehow bypass the signature and get an item that had a price less than or equal to 0.
Looking at the server code, we could tack on a `&price=0` to the end of our order string, after the signature. Since `b64decode` in `python2` ignores invalid characters added after the `=` padding, this left the signature intact and valid, and the payment code would set the price to 0 at the end.

Code: [exploit.py](exploit.py)
