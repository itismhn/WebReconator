import requests

SECURITY_HEADERS = [
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Referrer-Policy",
    "Permissions-Policy",
    "X-XSS-Protection",
    "Cross-Origin-Resource-Policy",
    "Cross-Origin-Embedder-Policy",
    "Cross-Origin-Opener-Policy",
    "Cache-Control",
    "Pragma",
    "Access-Control-Allow-Origin",
    "Access-Control-Allow-Methods",
    "Access-Control-Allow-Headers",
    "Server",
    "Set-Cookie",
]

def check_security_headers(url):
    try:
        try:
            response = requests.head(url, allow_redirects=True, timeout=10)
            if not response.headers:
                raise Exception("Empty headers with HEAD request.")
        except:
            print("[*] HEAD request failed or returned no headers. Trying GET...")
            response = requests.get(url, allow_redirects=True, timeout=10)

        headers = response.headers

        print(f"\n[+] Headers fetched from {url}:\n")
        for key, value in headers.items():
            print(f"{key}: {value}")

        print("\n[+] Checking for missing or weak security headers:\n")
        # check missing headers
        missing_headers = []
        warnings = []

        for header in SECURITY_HEADERS:
            if header not in headers:
                missing_headers.append(header)
            else:
                # Extra checks for some headers
                if header.lower() == "server":
                    if headers[header]:
                        warnings.append(f"[!] Server header present: {headers[header]} (consider removing).")
                if header.lower() == "set-cookie":
                    cookie_value = headers.get(header, "")
                    if "Secure" not in cookie_value or "HttpOnly" not in cookie_value:
                        warnings.append("[!] Set-Cookie header missing Secure or HttpOnly flags.")
        if missing_headers:
            print("[-] Missing Security Headers:")
            for mh in missing_headers:
                print(f"   - {mh}")
        else:
            print("[+] All important security headers are present. Well done!")
        if warnings:
            print("\n[!] Additional Warnings:")
            for warning in warnings:
                print(warning)

    except requests.exceptions.RequestException as e:
        print(f"[!] Error connecting to {url}: {e}")

if __name__ == "__main__":
    check_security_headers(target_url)