import socket
import threading
from datetime import datetime
import os
import time
import sys
import ipaddress
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse

class PortScanner:
    def __init__(self, target=None, threads=200, timeout=1):
        self.target = target
        self.threads = threads
        self.timeout = timeout
        self.open_ports = []
        self.lock = threading.Lock()
        
        # Popular ports for quick scanning
        self.common_ports = [
            21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 993, 995,
            1723, 3306, 3389, 5432, 5900, 6000, 6001, 8080, 8443, 8888, 9100
        ]

    def pulseEffect(self, text):
        pulse_colors = ['\033[90m', '\033[37m', '\033[97m', '\033[37m', '\033[90m']
        try:
            columns = os.get_terminal_size().columns
        except OSError:
            columns = 80

        for i in range(3):  # Reduce the number of pulses for greater speed
            for color in pulse_colors:
                os.system('cls' if os.name == 'nt' else 'clear')
                padding = (columns - len(text)) // 2 * " "
                print(color + padding + text + '\033[0m')
                time.sleep(0.005)  # Reduce latency

    def port_scanner_banner(self):
        banner_text = r'''
  ______    ______   _______   ________        ______    ______    ______   __    __  __    __  ________  _______  
/       \  /      \ /       \ /        |      /      \  /      \  /      \ /  \  /  |/  \  /  |/        |/       \ 
$$$$$$$  |/$$$$$$  |$$$$$$$  |$$$$$$$$/      /$$$$$$  |/$$$$$$  |/$$$$$$  |$$  \ $$ |$$  \ $$ |$$$$$$$$/ $$$$$$$  |
$$ |__$$ |$$ |  $$ |$$ |__$$ |   $$ | ______ $$ \__$$/ $$ |  $$/ $$ |__$$ |$$$  \$$ |$$$  \$$ |$$ |__    $$ |__$$ |
$$    $$/ $$ |  $$ |$$    $$<    $$ |/      |$$      \ $$ |      $$    $$ |$$$$  $$ |$$$$  $$ |$$    |   $$    $$< 
$$$$$$$/  $$ |  $$ |$$$$$$$  |   $$ |$$$$$$/  $$$$$$  |$$ |   __ $$$$$$$$ |$$ $$ $$ |$$ $$ $$ |$$$$$/    $$$$$$$  |
$$ |      $$ \__$$ |$$ |  $$ |   $$ |        /  \__$$ |$$ \__/  |$$ |  $$ |$$ |$$$$ |$$ |$$$$ |$$ |_____ $$ |  $$ |
$$ |      $$    $$/ $$ |  $$ |   $$ |        $$    $$/ $$    $$/ $$ |  $$ |$$ | $$$ |$$ | $$$ |$$       |$$ |  $$ |
$$/        $$$$$$/  $$/   $$/    $$/          $$$$$$/   $$$$$$/  $$/   $$/ $$/   $$/ $$/   $$/ $$$$$$$$/ $$/   $$/ 

Enhanced Port Scanner v2.0
made by: Amirprx3 (Enhanced)
github: https://github.com/Amirprx3
'''
        self.pulseEffect(banner_text)

    def validate_target(self, target):
        """Validate the target address"""
        try:
            # check IP address
            ipaddress.ip_address(target)
            return target
        except:
            try:
                # Convert hostname to IP
                ip = socket.gethostbyname(target)
                print(f"[*] Resolved {target} to {ip}")
                return ip
            except socket.gaierror:
                print(f"[!] Could not resolve hostname: {target}")
                return None

    def scan_port(self, target, port):
        """Single port scanning with optimization"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            
            # Use TCP_NODELAY for more speed
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            
            result = sock.connect_ex((target, port))
            sock.close()
            
            if result == 0:
                service = self.get_service_name(port)
                with self.lock:
                    self.open_ports.append(port)
                    print(f"\033[92m[+] Port {port}/tcp open\033[0m {service}")
                return port
        except Exception:
            pass
        return None

    def get_service_name(self, port):
        """Get service name for port"""
        common_services = {
            21: "(FTP)", 22: "(SSH)", 23: "(Telnet)", 25: "(SMTP)",
            53: "(DNS)", 80: "(HTTP)", 110: "(POP3)", 143: "(IMAP)",
            443: "(HTTPS)", 993: "(IMAPS)", 995: "(POP3S)",
            3306: "(MySQL)", 3389: "(RDP)", 5432: "(PostgreSQL)",
            6379: "(Redis)", 27017: "(MongoDB)"
        }
        return common_services.get(port, "")

    def scan_common_ports(self, target):
        """Popular port scanning"""
        print(f"\n[*] Scanning common ports on {target}...")
        print("-" * 50)
        
        with ThreadPoolExecutor(max_workers=50) as executor:
            futures = [executor.submit(self.scan_port, target, port) 
                      for port in self.common_ports]
            
            for future in as_completed(futures):
                future.result()

    def scan_range(self, target, start_port=1, end_port=65535):
        """Port range scanning"""
        print(f"\n[*] Scanning ports {start_port}-{end_port} on {target}...")
        print("-" * 50)
        
        try:
            with ThreadPoolExecutor(max_workers=self.threads) as executor:
                futures = [executor.submit(self.scan_port, target, port) 
                          for port in range(start_port, end_port + 1)]
                
                completed = 0
                total = end_port - start_port + 1
                
                for future in as_completed(futures):
                    future.result()
                    completed += 1
                    
                    # Show progress every 1000 ports
                    if completed % 1000 == 0:
                        progress = (completed / total) * 100
                        print(f"[*] Progress: {progress:.1f}% ({completed}/{total})")
                        
        except KeyboardInterrupt:
            print("\n[!] Scan interrupted by user")
            return

    def run_interactive(self):
        """Run interactive mode"""
        self.port_scanner_banner()
        
        # Get target
        target_input = input("\n[+] Target (IP/Hostname): ").strip()
        if not target_input:
            print("[!] Target cannot be empty")
            return
            
        target = self.validate_target(target_input)
        if not target:
            return
            
        self.target = target  # Set the target
            
        # Select scan type
        print("\nScan Options:")
        print("1) Quick scan (common ports)")
        print("2) Full scan (all ports 1-65535)")
        print("3) Custom range")
        
        try:
            choice = int(input("\n[+] Select scan type: "))
        except ValueError:
            print("[!] Invalid choice")
            return
            
        # Advanced settings
        try:
            threads = int(input(f"[+] Number of threads (default {self.threads}): ") or self.threads)
            self.threads = min(threads, 1000)  # max limit thread
        except ValueError:
            pass
            
        print(f"\n{'='*60}")
        print(f"Target: {target}")
        print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Threads: {self.threads}")
        print(f"{'='*60}")
        
        start_time = time.time()
        
        try:
            if choice == 1:
                self.scan_common_ports(target)
            elif choice == 2:
                self.scan_range(target)
            elif choice == 3:
                try:
                    start = int(input("[+] Start port: "))
                    end = int(input("[+] End port: "))
                    if start > end or start < 1 or end > 65535:
                        print("[!] Invalid port range")
                        return
                    self.scan_range(target, start, end)
                except ValueError:
                    print("[!] Invalid port numbers")
                    return
            else:
                print("[!] Invalid choice")
                return
                
        except KeyboardInterrupt:
            print("\n[!] Scan interrupted")
            
        end_time = time.time()
        scan_time = end_time - start_time
        
        # show result
        print(f"\n{'='*60}")
        print(f"Scan completed in {scan_time:.2f} seconds")
        print(f"Open ports found: {len(self.open_ports)}")
        
        if self.open_ports:
            print("\nOpen Ports Summary:")
            print("-" * 30)
            for port in sorted(self.open_ports):
                service = self.get_service_name(port)
                print(f"  {port}/tcp {service}")
        else:
            print("\n[*] No open ports found")
            
        input("\nPress Enter to continue...")

    def run_scan(self, target, scan_type="common", start_port=1, end_port=65535, threads=200):
        """Run scan programmatically (for use from other modules)"""
        self.target = target
        self.threads = threads
        self.open_ports = []  # Reset open ports
        
        validated_target = self.validate_target(target)
        if not validated_target:
            return None
            
        print(f"\n[*] Starting scan on {validated_target}")
        start_time = time.time()
        
        try:
            if scan_type == "common":
                self.scan_common_ports(validated_target)
            elif scan_type == "full":
                self.scan_range(validated_target, 1, 65535)
            elif scan_type == "range":
                self.scan_range(validated_target, start_port, end_port)
        except KeyboardInterrupt:
            print("\n[!] Scan interrupted")
            
        end_time = time.time()
        scan_time = end_time - start_time
        
        return {
            'target': validated_target,
            'open_ports': sorted(self.open_ports),
            'scan_time': scan_time,
            'total_ports': len(self.open_ports)
        }

def main():
    """Main function"""
    try:
        scanner = PortScanner()  # No required arguments now
        scanner.run_interactive()
    except KeyboardInterrupt:
        print("\n[!] Program interrupted")
        sys.exit(0)
    except Exception as e:
        print(f"[!] Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()