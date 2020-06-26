#!/usr/bin/env python3

# find password and pass to the process and start the priveleged shell
# then just cat /challenges/flag0 and you can see the content
password = 'p4sSw0Rd\n' # \n is not the part of password. it needed so scanf can catch it.

from pwn import *

p = process('/challenges/chal0')
p.send(password)
p.interactive()
