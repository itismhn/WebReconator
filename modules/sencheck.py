import requests

def check_important_files(domain):
    if not domain.startswith("http"):
        domain = "http://" + domain

    files = {
        "robots.txt",
        ".git/config",
        ".env",
        ".htaccess",
        ".DS_Store",
        "sitemap.xml"
    }

    print(f"\n[+] Scanning for exposed files on: {domain}\n")
    for path in files:
        url = f"{domain.rstrip('/')}/{path}"
        try:
            response = requests.get(url, timeout=5)
            status = response.status_code

            if status == 200:
                print(f"[FOUND] {url} (200 OK)")
            elif status == 403:
                print(f"[POSSIBLY EXISTS] {url} (403 Forbidden)")
            elif status == 200:
                print(f"[CHECK] {url} (200 OK, but signature missing)")
            else:
                print(f"[NOT FOUND] {url} ({status})")

        except requests.RequestException as e:
            print(f"[ERROR] {url}: {e}")
