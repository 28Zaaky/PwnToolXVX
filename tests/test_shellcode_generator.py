import unittest
from shellcode_generator import ShellcodeGenerator

class TestShellcodeGenerator(unittest.TestCase):
    def test_generate_shellcode(self):
        generator = ShellcodeGenerator()
        shellcode = generator.generate_shellcode()
        self.assertIsInstance(shellcode, bytes)

if __name__ == "__main__":
    unittest.main()