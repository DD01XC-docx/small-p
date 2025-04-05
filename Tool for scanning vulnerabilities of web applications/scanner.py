import concurrent.futures
from sql_injection import check_sql_injection
from xss import xss_checker
from csrf import csrf_checker
from report import generate_json_report, generate_html_report


def scan(url):
    vulnerabilities = []

    if check_sql_injection(url):
        vulnerabilities.append(f"SQL injection detected at {url}")

    if xss_checker(url):
        vulnerabilities.append(f"XSS vulnerability detected at {url}")

    if csrf_checker(url):
        vulnerabilities.append(f"CSRF vulnerability detected at {url}")

    return vulnerabilities


def scan_urls(urls):
    all_vulnerabilities = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(scan, urls)
        for result in results:
            all_vulnerabilities.extend(result)

    generate_json_report(all_vulnerabilities)
    generate_html_report(all_vulnerabilities)

    return all_vulnerabilities


if __name__ == '__main__':
    urls_to_scan = [
        "http://example.com/login",
        "https://example.com/search",
    ]

    vulnerabilities = scan_urls(urls_to_scan)

    if vulnerabilities:
        print("Vulnerabilities found:")
        for vuln in vulnerabilities:
            print(vuln)
    else:
        print("No vulnerabilities found.")

