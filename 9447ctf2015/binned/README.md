# binned

Running the program with `strace` shows that it's doing a lot of weird syscalls
between the printed messages. We suspect that the syscall values might spell out
something, but `strace` is too nice and gives human-readable names for each
syscall :/

We grabbed [ministrace](https://github.com/nelhage/ministrace) and parsed the
resulting output in python to get the flag.

```
Flag: 9447{Ch3ck_0uT_My_C411iNg_C0dE}
```
