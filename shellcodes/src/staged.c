#include <stdio.h>
#include <unistd.h>
#include <sys/mman.h>

int main() {
    unsigned char buffer[256];
    
    puts("Entrez votre shellcode : ");
    read(0, buffer, 0x15);
    
    // Rend la stack exécutable
    void *page = (void *)((unsigned long)buffer & ~0xFFF);
    mprotect(page, 4096, PROT_READ | PROT_WRITE | PROT_EXEC);
    
    // Exécute
    void (*func)() = (void (*)())buffer;
    func();
    
    return 0;
}
