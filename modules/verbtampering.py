import requests
http_methods = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS', 'PATCH', 'TRACE', 'CONNECT']
def http_requests(URL):
    for method in http_methods:
        try:
            response = requests.request(method, URL)
            print(f"[~] {method} {response.status_code} {response.reason}")
        except requests.exceptions.RequestException as e:
            print(f"[!] {method} request failed: {e}")