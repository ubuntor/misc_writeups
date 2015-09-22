# Punchout
**TL;DR: EBCDIC Multitime Pad**

After a bunch of dead ends looking into punchcard flipping and lots of XORs, we found that this was a multitime pad, except in EBCDIC instead of ASCII.

Searching around for words like " the " and " thousand " (see the comments in punch.py) eventually gave us the plaintext from the Project Gutenburg texts, and gave us this output:

```
0 'As it is possible that, in the many severe strictures passed, in the
course of this work, upon the Dutch Administration in Java, some of
the observations may, for want of a careful restriction in the words
employed, appear to extend to the Dutch nation and character generally,
I think it proper explicitly to declare, that such observations
are intended exclusively to apply to the Colonial Government and
its Officers. The orders of the Dutch Government in Holland to the
Authorities at Batavia, as far as my information extends, breathe a
spirit of liberality and benevolence; and I have reason to believe,
that the tyranny and rapacity of its colonial officers, created no less
indignation in Holland than in other countries of Europe.

flag{https://i.imgzá.þ[m/ZNem5o3.gifv}

That's the flÐH You should submit that to the score server.'
```

Some of it's corrupted because the fancy quotes and apostrophes don't translate well into EBCDIC, but that flag looks like an i.imgur.com url.
```
Flag: flag{https://i.imgur.com/ZNem5o3.gifv}
```
