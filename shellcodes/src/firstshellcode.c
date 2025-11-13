#include <stdio.h>
#include <unistd.h>
#include <sys/mman.h>

int main() {
    unsigned char buffer[256];
    void (*func)() = (void (*)())buffer;
    puts("Entrez votre shellcode : ");
    read(0, buffer, sizeof(buffer));
    
    // Rend la stack exécutable
    void *page = (void *)((unsigned long)buffer & ~0xFFF);
    mprotect(page, 4096, PROT_READ | PROT_WRITE | PROT_EXEC);
    
    // Exécute le shellcode
    func();
    
    return 0;
}
