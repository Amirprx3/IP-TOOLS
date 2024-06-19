import socket
import os
import time

def pulseEffect(text):
    pulse_colors = ['\033[90m', '\033[37m', '\033[97m', '\033[37m', '\033[90m']
    columns = os.get_terminal_size().columns

    for i in range(5):
        for color in pulse_colors:
            os.system('cls' if os.name == 'nt' else 'clear')
            padding = (columns - len(text)) // 2 * " "
            print(color + padding + text + '\033[0m')
            time.sleep(0.01)

def ip_finder_banner():
    pulseEffect(
        '''
 ______  _______           ________  ______  __    __  _______   ________  _______  
/      |/       \         /        |/      |/  \  /  |/       \ /        |/       \ 
$$$$$$/ $$$$$$$  |        $$$$$$$$/ $$$$$$/ $$  \ $$ |$$$$$$$  |$$$$$$$$/ $$$$$$$  |
  $$ |  $$ |__$$ | ______ $$ |__      $$ |  $$$  \$$ |$$ |  $$ |$$ |__    $$ |__$$ |
  $$ |  $$    $$/ /      |$$    |     $$ |  $$$$  $$ |$$ |  $$ |$$    |   $$    $$< 
  $$ |  $$$$$$$/  $$$$$$/ $$$$$/      $$ |  $$ $$ $$ |$$ |  $$ |$$$$$/    $$$$$$$  |
 _$$ |_ $$ |              $$ |       _$$ |_ $$ |$$$$ |$$ |__$$ |$$ |_____ $$ |  $$ |
/ $$   |$$ |              $$ |      / $$   |$$ | $$$ |$$    $$/ $$       |$$ |  $$ |
$$$$$$/ $$/               $$/       $$$$$$/ $$/   $$/ $$$$$$$/  $$$$$$$$/ $$/   $$/ 
                        
made by: Amirprx3
github: https://github.com/Amirprx3

        '''
    )
    
def ip_finder():
    host_input = input(str('[+] Url: '))
    host = socket.gethostbyname(host_input)
    print(f"IP: {host}\n")
    input()

if __name__ == "__main__":
    ip_finder()
