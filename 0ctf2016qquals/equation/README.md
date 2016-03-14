# Equation

Looking at the image, we get the last half of the private key. Base64 decoding this gives us the raw bytes of the ASN.1 format, from which we can extract the following:

```
q = 0x...3acf6684e41176a5b673056b9cd23bd832dc017a57509d471b (missing first half)
d mod (p-1) = 0x00d5a225c0d41b16699c4471570eecd3dd7759736d5781aa7710b31b4a46e441d386da1345bc97d1aa913f853f850f6d4684a80e6067fb71cf213b276c2cbaed59
d mod (q-1) = 0x1338c593d3b5428ce978bed7a553527155b3d138aeac084020c0c67f54b953015e55f60a5d31386505e02e6122dad7db0a05ecb552e448b347adc2c9170fa2f3
coefficient = 0x00d5c8d6dc583ecdf3c321663ba32ae4ab1c9a2ded6702691993184209e93914f0d5adf415634788d5919d84a8d77429959d40fba47b29cf70b943124217c9a431
```

Using [this paper](https://eprint.iacr.org/2004/147.pdf), we can recover `e`, `p`, and `q` from `d mod (p-1)` and `d mod (q-1)`. Popping those into `rsatool` gives us the full private key with which we can decode the flag.


Code: [equation.py](equation.py)

```
Flag: 0ctf{Keep_ca1m_and_s01ve_the_RSA_Eeeequati0n!!!}
```
