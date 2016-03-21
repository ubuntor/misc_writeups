from pwn import *
r = remote('104.199.132.199',2223)

s = r.recvuntil('zeros.\n')
prefix = s.split("'")[1]
print(s,prefix)

submit = iters.mbruteforce(lambda x: sha256sumhex(prefix+x)[:5] == '00000', string.ascii_letters + string.digits, length = 63-len(prefix))

r.sendline(prefix+submit)

board = ''
oldboard = ''
first = ''
p = None

while True:
    s = ''
    try:
        s = r.recvuntil(('}','?'))
    except EOFError:
        print(r.clean(0))
        break
    print(s)
    print(r.clean(0))
    board = s.split('012345678901\n')[-1].split('Column')[0]
    print(`board`)
    if '###' in s: # new game
        first = 'yes' if 'white' in s else 'no' # is remote playing first?
        print(first)
        oldboard = ('.'*12+'\n')*12
        p = process('./connect_four')
        p.sendline('2' if first == 'yes' else '1')
        if first == 'no':
            # get local's move
            s2 = p.recvuntil('>>>')
            print(s2)
            localmove = s2.rstrip('>').split('<<<')[1]
            print('localmove:',localmove)
            # and apply it to remote
            r.sendline(localmove)
    if not ('###' in s and first == 'no'):
        # get remote's move
        print(board,oldboard)
        newmoves = [(i, board[i]) for i in range(min(len(board),len(oldboard))) if board[i] != oldboard[i]]
        print(newmoves)
        remotemove = '0'
        for move in newmoves:
            if (move[1] == 'o' and first == 'yes') or (move[1] == 'x' and first == 'no'):
                remotemove = str(move[0]%13)
                break
        # and apply it to local
        print(p.recvuntil('move: '))
        print('remotemove:',remotemove)
        p.sendline(remotemove)
        # then get local's move
        s2 = p.recvuntil('>>>')
        print(s2)
        localmove = s2.rstrip('>').split('<<<')[1]
        print('localmove:',localmove)
        # and apply it to remote
        r.sendline(localmove)
    oldboard = board
