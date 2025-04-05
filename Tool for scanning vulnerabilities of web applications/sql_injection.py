import requests

def check_sql_injection(url):
    payload = ["' OR 1=1 --", '" OR 1=1 --', "' OR 'a'='a", '" OR "a"="a"']
    try:
        response = requests.get(url, params={'q': payload})
        if response.status_code == 200 and 'error' in response.text:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error checking SQL injection for {url}: {e}")
        return False
