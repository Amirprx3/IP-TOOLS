import socket
from datetime import datetime
import os
import time
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

def pulseEffect(text):
    pulse_colors = ['\033[90m', '\033[37m', '\033[97m', '\033[37m', '\033[90m']
    columns = os.get_terminal_size().columns

    for i in range(5):
        for color in pulse_colors:
            os.system('cls' if os.name == 'nt' else 'clear')
            padding = (columns - len(text)) // 2 * " "
            print(color + padding + text + '\033[0m')
            time.sleep(0.01)

def port_scanner_banner():
    pulseEffect(
        '''
  ______    ______   _______   ________        ______    ______    ______   __    __  __    __  ________  _______  
/       \  /      \ /       \ /        |      /      \  /      \  /      \ /  \  /  |/  \  /  |/        |/       \ 
$$$$$$$  |/$$$$$$  |$$$$$$$  |$$$$$$$$/      /$$$$$$  |/$$$$$$  |/$$$$$$  |$$  \ $$ |$$  \ $$ |$$$$$$$$/ $$$$$$$  |
$$ |__$$ |$$ |  $$ |$$ |__$$ |   $$ | ______ $$ \__$$/ $$ |  $$/ $$ |__$$ |$$$  \$$ |$$$  \$$ |$$ |__    $$ |__$$ |
$$    $$/ $$ |  $$ |$$    $$<    $$ |/      |$$      \ $$ |      $$    $$ |$$$$  $$ |$$$$  $$ |$$    |   $$    $$< 
$$$$$$$/  $$ |  $$ |$$$$$$$  |   $$ |$$$$$$/  $$$$$$  |$$ |   __ $$$$$$$$ |$$ $$ $$ |$$ $$ $$ |$$$$$/    $$$$$$$  |
$$ |      $$ \__$$ |$$ |  $$ |   $$ |        /  \__$$ |$$ \__/  |$$ |  $$ |$$ |$$$$ |$$ |$$$$ |$$ |_____ $$ |  $$ |
$$ |      $$    $$/ $$ |  $$ |   $$ |        $$    $$/ $$    $$/ $$ |  $$ |$$ | $$$ |$$ | $$$ |$$       |$$ |  $$ |
$$/        $$$$$$/  $$/   $$/    $$/          $$$$$$/   $$$$$$/  $$/   $$/ $$/   $$/ $$/   $$/ $$$$$$$$/ $$/   $$/ 

made by: Amirprx3
github: https://github.com/Amirprx3

        '''
    )

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            return f"[+] Port {port}: Open"
        sock.close()
    except Exception as e:
        return None
    return None

def scan(target):
    open_ports = []
    try:
        with ThreadPoolExecutor(max_workers=500) as executor:
            futures = [executor.submit(scan_port, target, port) for port in range(1, 65536)]
            for future in as_completed(futures):
                result = future.result()
                if result:
                    print(result)
                    open_ports.append(result)
    except KeyboardInterrupt:
        print("\nExiting Program.")
        sys.exit()
    except socket.gaierror:
        print("\nHostname Could Not Be Resolved.")
        sys.exit()
    except socket.error:
        print("\nServer not responding.")
        sys.exit()

def main():
    port_scanner_banner()
    target = input("[+] Target IP: ")

    print("_" * 50)
    print("Scanning Target: " + target)
    current_time = datetime.now().time().strftime("%H:%M:%S")
    print("Scanning started at: " + current_time)
    print("_" * 50)
    scan(target)

if __name__ == "__main__":
    main()