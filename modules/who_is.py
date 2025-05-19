import whois

def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        return w
    except Exception as e:
        print(f"[ERROR] Failed to fetch WHOIS for {domain}: {e}")
        return None

def display_whois_info(whois_data):
    if not whois_data:
        print("No WHOIS data to display.")
        return

    print("\n[+] WHOIS Information:")
    try:
        print(f"Domain Name: {whois_data.domain_name}")
        print(f"Registrar: {whois_data.registrar}")
        print(f"Creation Date: {whois_data.creation_date}")
        print(f"Expiration Date: {whois_data.expiration_date}")
        print(f"Name Servers: {', '.join(whois_data.name_servers) if whois_data.name_servers else 'N/A'}")
    except Exception as e:
        print(f"[ERROR] Failed to display WHOIS info: {e}")