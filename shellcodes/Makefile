CC = gcc
CFLAGS = -z execstack -fno-stack-protector

all: firstshellcode no-null-byte staged seccomp_whitelist

first: src/firstshellcode.c
	$(CC) $(CFLAGS) -o firstshellcode src/firstshellcode.c

firstshellcode: src/firstshellcode.c
	$(CC) $(CFLAGS) -o firstshellcode src/firstshellcode.c

no-null-byte: src/no-null-byte.c
	$(CC) $(CFLAGS) -o no-null-byte src/no-null-byte.c

staged: src/staged.c
	$(CC) $(CFLAGS) -o staged src/staged.c

seccomp_whitelist: src/seccomp_whitelist.c
	$(CC) $(CFLAGS) -o seccomp_whitelist src/seccomp_whitelist.c
	
re: clean all

clean:
	rm -f firstshellcode no-null-byte staged seccomp_whitelist

.PHONY: all clean re