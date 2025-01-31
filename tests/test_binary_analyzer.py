import unittest
from binary_analyzer import BinaryAnalyzer

class TestBinaryAnalyzer(unittest.TestCase):
    def test_analyze(self):
        analyzer = BinaryAnalyzer("vulnerable_binary")
        vulnerabilities = analyzer.analyze()
        self.assertIsInstance(vulnerabilities, list)
        analyzer.close()

if __name__ == "__main__":
    unittest.main()