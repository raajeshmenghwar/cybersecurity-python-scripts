#!/usr/bin/python3

from pwn import *

s1 = ssh(host="127.0.0.1",user="kali",password="kali")
#p1 = s1.shell("sh")
#p1.interactive()


p2 = s1.process(["nmap","127.0.0.1"])
out = p2.recvall()
print(out.decode())