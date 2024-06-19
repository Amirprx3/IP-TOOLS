import os
import time
import port_scanner
import IP_finder
import random

def neonEffect(text):
    neon_colors = ["\033[1;30;40m"]
    for char in text:
        print(neon_colors[0] + char, end="", flush=True)
        neon_colors.append(neon_colors.pop(0))
        time.sleep(0.001)
    print('\033[0m')

def main_banner():
    neonEffect(
        f'''
1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
░▒▓█▓▒░▒▓███████▓▒░▒1111▓████████▓▒░▒▓██████▓▒░1░▒▓██████▓▒░░▒▓█▓▒░1111111░▒▓███████▓▒░1
░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░111111░▒▓█▓▒░11░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░111111░▒▓█▓▒░1111111
░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░111111░▒▓█▓▒░11░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░111111░▒▓█▓▒░1111111
░▒▓█▓▒░▒▓███████▓▒░1111111░▒▓█▓▒░11░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░1111111░▒▓██████▓▒░1
░▒▓█▓▒░▒▓█▓▒░1111111111111░▒▓█▓▒░11░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░1111111111111░▒▓█▓▒░
░▒▓█▓▒░▒▓█▓▒░1111░▒▓█▓▒░11░▒▓█▓▒░11░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░1111111111111░▒▓█▓▒░
░▒▓█▓▒░▒▓█▓▒░1111111111111░▒▓█▓▒░11░▒▓██████▓▒░1░▒▓██████▓▒░░▒▓████████▓▒░▒▓███████▓▒░11
1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111
Version | 1.0 11111111111111111111111111111111111111111111111111111111111111111111111111
made by: Amirprx3 1111111111111111111111111111111111111111111111111111111111111111111111
github: https://github.com/Amirprx3 1111111111111111111111111111111111111111111111111111
        '''
    )

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        main_banner()
        try:
            user_choice = int(input("1) IP-FINDER\n2) PORT-SCANNER\n\n[+] Please select a tool ==> "))
            if user_choice == 1:
                print("\nLoding", end='', flush=True)
                for _ in range(random.randrange(3,8)):
                    time.sleep(0.5)  
                    print(".", end='', flush=True)

                print("\r" + " " * 20 + "\r", end='')
                os.system('cls' if os.name == 'nt' else 'clear')
                IP_finder.ip_finder_banner()
                IP_finder.ip_finder()
            elif user_choice == 2:
                print("\nLoding", end='', flush=True)
                for _ in range(random.randrange(3, 8)):
                    time.sleep(0.5)  
                    print(".", end='', flush=True)

                print("\r" + " " * 20 + "\r", end='')
                os.system('cls' if os.name == 'nt' else 'clear')
                port_scanner.port_scanner_banner()
                port_scanner.main()
            else:
                print("\nPlease enter 1 or 2")
        except ValueError:
            print("\nPlease enter a valid number")
            time.sleep(1)

if __name__ == "__main__":
    main()
