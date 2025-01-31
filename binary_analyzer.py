import r2pipe

class BinaryAnalyzer:
    def __init__(self, binary_path):
        self.binary_path = binary_path
        self.r2 = r2pipe.open(binary_path)

    def analyze(self):
        self.r2.cmd('aaaa')  
        vuln_functions = self._find_vulnerable_functions()
        return vuln_functions

    def _find_vulnerable_functions(self):
        vuln_functions = []
        functions = self.r2.cmdj('aflj')
        for func in functions:
            if 'gets' in func['name'] or 'strcpy' in func['name']:
                vuln_functions.append(func['name'])
        return vuln_functions

    def close(self):
        self.r2.quit()