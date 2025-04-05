import json
from datetime import datetime


def generate_json_report(vulnerabilities):
    report = {
        'timestamp': str(datetime.now()),
        'vulnerabilities': vulnerabilities
    }

    try:
        with open('vulnerabilities_report.json', 'w') as f:
            json.dump(report, f, indent=4)
    except Exception as e:
        print(f"Error generating JSON report: {e}")


def generate_html_report(vulnerabilities):
    report = "<html><body><h1>Vulnerabilities Report</h1><ul>"

    for vuln in vulnerabilities:
        report += f"<li>{vuln}</li>"

    report += "</ul></body></html>"

    try:
        with open('vulnerabilities_report.html', 'w') as f:
            f.write(report)
    except Exception as e:
        print(f"Error generating HTML report: {e}")
