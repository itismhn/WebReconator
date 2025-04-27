from modules.headersafe import check_security_headers

def show_menu():
    print("\n====== WebReconator ======")
    print("1. HeaderSafe (Check Security Headers)")
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
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("[!] Invalid choice, try again.")

if __name__ == "__main__":
    main()