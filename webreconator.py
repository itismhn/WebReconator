from modules.headersafe import check_security_headers
from modules.verbtampering import http_requests
from modules.sencheck import check_important_files
from modules.who_is import get_whois_info, display_whois_info
def show_menu():
    print("\n====== WebReconator ======")
    print("1. HeaderSafe (Check Security Headers)")
    print("2. Verb Tampering (Check HTTP Methods)")
    print("3. Sensitive Directory Check")
    print("4. Whois the domain")

    print("0. Exit!")
    print("==========================")

def main():
    url=input("Enter the URL (include http/https): ").strip()
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
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("[!] Invalid choice, try again.")

if __name__ == "__main__":
    main()