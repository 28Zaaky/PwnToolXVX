import argparse
from binary_analyzer import BinaryAnalyzer
from protection_checker import ProtectionChecker
from shellcode_generator import ShellcodeGenerator
from exploit_executor import ExploitExecutor
from report_generator import ReportGenerator

def main():
    parser = argparse.ArgumentParser(description="Outil de pentesting pour analyser et exploiter des binaires.")
    parser.add_argument('-f', '--file', required=True, help="Chemin vers le binaire à analyser.")
    args = parser.parse_args()

    binary_path = args.file

    # Analyse du binaire
    analyzer = BinaryAnalyzer(binary_path)
    vulnerabilities = analyzer.analyze()
    analyzer.close()

    # Vérification des protections
    checker = ProtectionChecker(binary_path)
    protections = checker.check_protections()

    # Génération du shellcode
    shellcode_gen = ShellcodeGenerator()
    shellcode = shellcode_gen.generate_shellcode()

    # Exécution du shellcode
    executor = ExploitExecutor(binary_path)
    executor.execute_shellcode(shellcode)

    # Génération du rapport
    report_gen = ReportGenerator()
    report = report_gen.generate_report(vulnerabilities, protections, shellcode, "Exploit réussi")

    # Affichage du rapport
    print("Rapport d'analyse pour le binaire :", binary_path)
    print("1. Vulnérabilités détectées :", report['Vulnerabilities'])
    print("2. Protections détectées :", report['Protections'])
    print("3. Shellcode généré :", report['Shellcode'])
    print("4. Résultat de l'exploitation :", report['Exploit Result'])

if __name__ == "__main__":
    main()