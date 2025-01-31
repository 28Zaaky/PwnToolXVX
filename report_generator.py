class ReportGenerator:
    def generate_report(self, vulnerabilities, protections, shellcode, exploit_result):
        report = {
            'Vulnerabilities': vulnerabilities,
            'Protections': protections,
            'Shellcode': shellcode,
            'Exploit Result': exploit_result
        }
        return report