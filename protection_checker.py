from pwn import *

class ProtectionChecker:
    def __init__(self, binary_path):
        self.binary_path = binary_path

    def check_protections(self):
        protections = {}
        elf = ELF(self.binary_path)
        protections['ASLR'] = elf.aslr
        protections['DEP'] = elf.nx
        protections['Stack Canaries'] = elf.canary
        return protections