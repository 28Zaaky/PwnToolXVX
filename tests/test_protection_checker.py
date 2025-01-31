import unittest
from protection_checker import ProtectionChecker

class TestProtectionChecker(unittest.TestCase):
    def test_check_protections(self):
        checker = ProtectionChecker("vulnerable_binary")
        protections = checker.check_protections()
        self.assertIsInstance(protections, dict)
        self.assertIn('ASLR', protections)
        self.assertIn('DEP', protections)
        self.assertIn('Stack Canaries', protections)

if __name__ == "__main__":
    unittest.main()