#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <sys/mman.h>

int main() {
    unsigned char buffer[256];
    unsigned char exec_buffer[256];
    
    puts("Entrez votre shellcode : ");
    int n = read(0, buffer, sizeof(buffer));
    
    // Copie avec strncpy
    strncpy((char *)exec_buffer, (char *)buffer, n);
    
    // Rend la zone exécutable
    void *page = (void *)((unsigned long)exec_buffer & ~0xFFF);
    mprotect(page, 4096, PROT_READ | PROT_WRITE | PROT_EXEC);
    
    // Exécute
    void (*func)() = (void (*)())exec_buffer;
    func();
    
    return 0;
}
