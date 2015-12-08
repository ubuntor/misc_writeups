# the *real* flag finder

Unfortunately, running the program doesn't print the flag :(
However, running the program in `gdb` and breaking at the final flag comparison
(`0x400729`) gives us the flag on the stack.

```
Flag: 9447{C0ngr47ulaT1ons_p4l_buddy_y0Uv3_solved_the_re4l__H4LT1N6_prObL3M}
```
