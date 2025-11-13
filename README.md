# Deep Dive into the Shellcode World: Bypassing Modern Protections

## Contexte

Présentation sur le shellcoding et le contournement des certaines protections en sécurité offensive. Cette présentation a été réalisée dans le cadre d'une conférence et explore différentes techniques d'exploitation et de bypass de mécanismes de sécurité.

## Objectifs

- Comprendre les bases des shellcodes en assembleur x64
- Maîtriser les techniques de bypass de protections courantes
- Explorer des méthodes avancées de contournement (staged shellcodes, seccomp bypass)
- Démontrer que même les protections modernes peuvent être contournées avec créativité

## Structure du répertoire
```
.
├── README.md                    # Ce fichier
├── shellcodes/                  # Code source et exploits
│   ├── src/                     # Programmes C vulnérables
│   │   ├── firstshellcode.c     # Programme basique pour injection
│   │   ├── no-null-byte.c       # Challenge avec strncpy
│   │   ├── staged.c             # Challenge avec limitation de taille
│   │   └── seccomp_whitelist.c  # Challenge avec protection seccomp
│   ├── firstshellcode.py        # Exploit : premier shellcode execve
│   ├── no-null-byte.py          # Exploit : bypass null bytes
│   ├── staged.py                # Exploit : shellcode en 2 étapes
│   ├── seccomp.py               # Exploit : bypass seccomp via mode 32 bits
│   ├── Makefile                 # Compilation des challenges
│   └── flag.txt                 # Flag à capturer
└── slides/                      # Présentation
    ├── prez.pdf                 # Présentation au format PDF
    └── prez.pptx                # Présentation au format PowerPoint

```

## Compilation et utilisation

### Compiler les challenges
```bash
cd shellcodes
make
```

### Lancer un challenge
```bash
./firstshellcode      # Challenge basique
./no-null-byte        # Challenge avec null bytes
./staged              # Challenge avec taille limitée
./seccomp_whitelist   # Challenge avec seccomp
```

### Exécuter les exploits
```bash
python3 firstshellcode.py
python3 no-null-byte.py
python3 staged.py
python3 seccomp.py
```

## Techniques abordées

### 1. **My First Shellcode**
- Introduction aux shellcodes en x64
- Appel système `execve("/bin/sh")`
- Injection basique de code

### 2. **Bypass Null Bytes**
- Problème : `strncpy()` s'arrête au premier `\x00`
- Solution : 
  - Utilisation de `xor` pour mettre à zéro
  - Doubler les slashes (`//bin/sh`)
  - Utilisation de petits registres (`mov al, 59`)

### 3. **Staged Shellcodes**
- Problème : Limitation de taille (22 bytes)
- Solution : Shellcode en 2 étapes
  - Stage 1 : Lit le stage 2 depuis stdin
  - Stage 2 : Shellcode complet

### 4. **Seccomp Whitelist Bypass**
- Problème : Whitelist stricte de syscalls en 64 bits
- Solution : Basculer en mode 32 bits
  - Les numéros de syscalls 32 bits sont différents
  - Utilisation de `retfq` pour changer d'architecture

