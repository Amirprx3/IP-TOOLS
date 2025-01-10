import whois
import sys
import os
import time

IMPORTANT_KEYS = [
    "domain_name", 
    "creation_date", 
    "expiration_date", 
    "updated_date", 
    "status", 
    "registrar", 
    "name_servers", 
    "emails", 
    "owner",
    "registrant"
]

def pulseEffect(text):
    pulse_colors = ['\033[90m', '\033[37m', '\033[97m', '\033[37m', '\033[90m']
    try:
        columns = os.get_terminal_size().columns
    except OSError:
        columns = 80

    for i in range(5):
        for color in pulse_colors:
            os.system('cls' if os.name == 'nt' else 'clear')
            padding = (columns - len(text)) // 2 * " "
            print(color + padding + text + '\033[0m')
            time.sleep(0.01)

def check_whois_banner():
    pulseEffect(
        '''
  ______   __    __  ________   ______   __    __        __       __  __    __   ______   ______   ______  
 /      \ /  |  /  |/        | /      \ /  |  /  |      /  |  _  /  |/  |  /  | /      \ /      | /      \ 
/$$$$$$  |$$ |  $$ |$$$$$$$$/ /$$$$$$  |$$ | /$$/       $$ | / \ $$ |$$ |  $$ |/$$$$$$  |$$$$$$/ /$$$$$$  |
$$ |  $$/ $$ |__$$ |$$ |__    $$ |  $$/ $$ |/$$/ ______ $$ |/$  \$$ |$$ |__$$ |$$ |  $$ |  $$ |  $$ \__$$/ 
$$ |      $$    $$ |$$    |   $$ |      $$  $$< /      |$$ /$$$  $$ |$$    $$ |$$ |  $$ |  $$ |  $$      \ 
$$ |   __ $$$$$$$$ |$$$$$/    $$ |   __ $$$$$  \$$$$$$/ $$ $$/$$ $$ |$$$$$$$$ |$$ |  $$ |  $$ |   $$$$$$  |
$$ \__/  |$$ |  $$ |$$ |_____ $$ \__/  |$$ |$$  \       $$$$/  $$$$ |$$ |  $$ |$$ \__$$ | _$$ |_ /  \__$$ |
$$    $$/ $$ |  $$ |$$       |$$    $$/ $$ | $$  |      $$$/    $$$ |$$ |  $$ |$$    $$/ / $$   |$$    $$/ 
 $$$$$$/  $$/   $$/ $$$$$$$$/  $$$$$$/  $$/   $$/       $$/      $$/ $$/   $$/  $$$$$$/  $$$$$$/  $$$$$$/  

made by: Amirprx3
github: https://github.com/Amirprx3  
        '''
    )

def check_whois(domain):
    try:
        w = whois.whois(domain)
        if not w:
            print(f"No WHOIS data found for {domain}")
            sys.exit(1)
        return w
    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit(1)

def filter_important_info(whois_data):
    important_info = {}
    for key in IMPORTANT_KEYS:
        if key in whois_data and whois_data[key]:
            value = whois_data[key]
            if isinstance(value, list):
                value = ", ".join(str(v) for v in value)
            important_info[key] = value
    return important_info

def main():
    domain = input("Enter domain name for WHOIS lookup: ")
    user_choice = input("Display 'all data' or 'important data'? ").strip().lower()
    print("--------------------------------------")

    if user_choice in ["all data", "all"]:
        whois_data = check_whois(domain)
        print("\n[+] Raw WHOIS Data:\n")
        print(whois_data)
    elif user_choice in ["important data", "important"]:
        whois_data = check_whois(domain)  # Ensure `whois_data` is set
        important_info = filter_important_info(whois_data)
        if important_info:
            print("\n[+] Important WHOIS Information:\n")
            for key, value in important_info.items():
                print(f"{key}: {value}")
        else:
            print("No important WHOIS information found.")
    else:
        print("Invalid choice. Please select 'all data' or 'important data'.")

    # Enter for return to main menu
    input("\n")

if __name__ == "__main__":
    main()
