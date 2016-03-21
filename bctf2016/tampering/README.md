# tampering

We're given a QR code with an odd pattern overlaid on top. Scanning the QR code gives us `The Flag is BCTF{~is^rete<Corrup_T!>>sf0rm_and_<**hidden*i**pi^tMre*>!}`. That first part looks like Discrete Corrupt Transform, so maybe it's referring to Discrete Cosine Transform?

To take the DCT of the image, we used the second algorithm in http://dsp.stackexchange.com/a/10606: mirror the QR code horizontally and vertically with GIMP, and use imagemagick's `convert` to take the FFT.

This gives us `BCTF{<<**hidden in QR code**>>_and_Reed_Solomon_algorithm!}` in the bottom right. The Reed Solomon algorithm is used for error correction, so maybe the QR code's error correction codes were tampered with.

We grabbed https://github.com/LazarSoft/jsqrcode, commented out the error correction part, and decoded the QR code to get `The Flag is BCTF{Discrete_Cosine_Transf0rm_and_<**hidden*in*picture*>!}`. Combining both parts gives us the flag.
