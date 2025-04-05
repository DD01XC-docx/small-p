import requests

def csrf_checker(url):
    try:
        response = requests.get(url)
        if 'csrf_token' not in response.text:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error checking CSRF for {url}: {e}")
        return False
