import requests

def xss_checker(url):
    payload = '<script>alert("XSS")</script>'
    try:
        response = requests.get(url, params={'q': payload})
        if payload in response.text:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error checking XSS for {url}: {e}")
        return False
