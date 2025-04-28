import requests
http_methods = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS', 'PATCH', 'TRACE', 'CONNECT']
def http_requests(URL):
    for method in http_methods:
        try:
            response = requests.request(method, URL, allow_redirects=False)
            print(f"[~] {method} => Status: {response.status_code} - {response.reason}")
            if response.status_code == 405:
                print(f"    [!] {method} is NOT allowed")
        except requests.exceptions.RequestException as e:
            print(f"[!] {method} request failed: {e}")