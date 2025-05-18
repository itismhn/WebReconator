import argparse
from modules.headersafe import check_security_headers
from modules.verbtampering import http_requests
from modules.sencheck import check_important_files
from modules.who_is import get_whois_info, display_whois_info
from modules.ssl_inspector import ssl_inspect

def show_menu():
    print("\n====== WebReconator ======")
    print("1. HeaderSafe (Check Security Headers)")
    print("2. Verb Tampering (Check HTTP Methods)")
    print("3. Sensitive Directory Check")
    print("4. Whois the domain")
    print("5. SSL Inspector (Get All Supported Cipher Suites)")
    print("0. Exit!")
    print("==========================")

def interactive_mode():
    try:
        url = input("\nEnter the URL (include http/https): ").strip()
        while True:
            show_menu()
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                check_security_headers(url)
                break
            elif choice == "2":
                http_requests(url)
                break
            elif choice == "3":
                check_important_files(url)
                break
            elif choice == "4":
                whois_data = get_whois_info(url)
                display_whois_info(whois_data)
                break
            elif choice == "5":
                ssl_inspect(url, 443)
                break
            elif choice == "0":
                print("Goodbye!")
                break
            else:
                print("[!] Invalid choice, try again.")
    except KeyboardInterrupt:
        print("\n[!] Program interrupted by user (CTRL+C).")

def run_all_modules(url):
    try:
        print("\n[+] Running all modules for:", url)
        check_security_headers(url)
        http_requests(url)
        check_important_files(url)
        whois_data = get_whois_info(url)
        display_whois_info(whois_data)
        ssl_inspect(url, 443)
    except KeyboardInterrupt:
        print("\n[!] Program interrupted by user (CTRL+C).")

def main():
    banner = r"""
 __      __   _    ___                      _           
 \ \    / /__| |__| _ \___ __ ___ _ _  __ _| |_ ___ _ _ 
  \ \/\/ / -_) '_ \   / -_) _/ _ \ ' \/ _` |  _/ _ \ '_|
   \_/\_/\___|_.__/_|_\___\__\___/_||_\__,_|\__\___/_|  """
    print(banner)

    parser = argparse.ArgumentParser(description="WebReconator - Web Reconnaissance Toolkit")
    parser.add_argument('-u', '--url', help='Target URL (include http/https) to run all modules')
    args = parser.parse_args()

    if args.url:
        run_all_modules(args.url.strip())
    else:
        interactive_mode()

if __name__ == "__main__":
    main()