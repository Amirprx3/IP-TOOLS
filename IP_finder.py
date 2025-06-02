import socket
import os
import time
import requests
import ipaddress
from concurrent.futures import ThreadPoolExecutor
import json

class IPFinder:
    def __init__(self):
        self.timeout = 5
        
    def pulseEffect(self, text):
        pulse_colors = ['\033[90m', '\033[37m', '\033[97m', '\033[37m', '\033[90m']
        try:
            columns = os.get_terminal_size().columns
        except OSError:
            columns = 80

        for i in range(3):
            for color in pulse_colors:
                os.system('cls' if os.name == 'nt' else 'clear')
                padding = (columns - len(text)) // 2 * " "
                print(color + padding + text + '\033[0m')
                time.sleep(0.005)

    def ip_finder_banner(self):
        self.pulseEffect(
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

Enhanced IP Finder v3.0                        
made by: Amirprx3 (Enhanced)
github: https://github.com/Amirprx3

            '''
        )

    def validate_input(self, host_input):
        """Input validation"""
        if not host_input.strip():
            return None, "Input cannot be empty"
            
        host_input = host_input.strip()
        
        # Delete the protocol if it exists.
        if host_input.startswith(('http://', 'https://')):
            host_input = host_input.replace('http://', '').replace('https://', '')
            
        # Delete path if it exists.
        if '/' in host_input:
            host_input = host_input.split('/')[0]
            
        return host_input, None

    def get_ip_basic(self, hostname):
        """Get the original IP"""
        try:
            ip = socket.gethostbyname(hostname)
            return ip
        except socket.gaierror as e:
            return None

    def get_all_ips(self, hostname):
        """Get all IPs associated with the domain"""
        try:
            ips = socket.gethostbyname_ex(hostname)
            return ips[2]  # IP Lists
        except socket.gaierror:
            return []

    def get_ip_geolocation(self, ip):
        """Get IP geolocation information"""
        try:
            # Use the free ipapi service
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=self.timeout)
            if response.status_code == 200:
                data = response.json()
                if data['status'] == 'success':
                    return {
                        'country': data.get('country', 'Unknown'),
                        'region': data.get('regionName', 'Unknown'),
                        'city': data.get('city', 'Unknown'),
                        'isp': data.get('isp', 'Unknown'),
                        'org': data.get('org', 'Unknown'),
                        'timezone': data.get('timezone', 'Unknown'),
                        'lat': data.get('lat', 'Unknown'),
                        'lon': data.get('lon', 'Unknown')
                    }
        except Exception:
            pass
        return None

    def check_ip_type(self, ip):
        """IP type detection"""
        try:
            ip_obj = ipaddress.ip_address(ip)
            if ip_obj.is_private:
                return "Private IP"
            elif ip_obj.is_loopback:
                return "Loopback IP"
            elif ip_obj.is_multicast:
                return "Multicast IP"
            elif ip_obj.is_reserved:
                return "Reserved IP"
            else:
                return "Public IP"
        except:
            return "Invalid IP"

    def reverse_dns_lookup(self, ip):
        """Reverse DNS lookup"""
        try:
            hostname = socket.gethostbyaddr(ip)[0]
            return hostname
        except:
            return None

    def check_port_connectivity(self, ip, ports=[80, 443, 22, 21]):
        """Checking connectivity to popular ports"""
        open_ports = []
        
        def check_port(port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                result = sock.connect_ex((ip, port))
                sock.close()
                if result == 0:
                    return port
            except:
                pass
            return None
        
        with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(check_port, port) for port in ports]
            for future in futures:
                result = future.result()
                if result:
                    open_ports.append(result)
                    
        return open_ports

    def ping_host(self, hostname):
        """It's pinging."""
        import subprocess
        import platform
        
        try:
            param = '-n' if platform.system().lower() == 'windows' else '-c'
            command = ['ping', param, '1', hostname]
            result = subprocess.run(command, capture_output=True, text=True, timeout=5)
            return result.returncode == 0
        except:
            return False

    def display_results(self, hostname, results):
        """Show results"""
        print(f"\n{'='*60}")
        print(f"Results for: {hostname}")
        print(f"{'='*60}")
        
        if results['primary_ip']:
            print(f"\033[92m[+] Primary IP: {results['primary_ip']}\033[0m")
            print(f"[+] IP Type: {results['ip_type']}")
            
            if results['reverse_dns']:
                print(f"[+] Reverse DNS: {results['reverse_dns']}")
                
            if results['is_reachable']:
                print(f"\033[92m[+] Host is reachable (ping successful)\033[0m")
            else:
                print(f"\033[91m[-] Host is not reachable (ping failed)\033[0m")
                
            if results['open_ports']:
                print(f"[+] Open ports: {', '.join(map(str, results['open_ports']))}")
            
        if len(results['all_ips']) > 1:
            print(f"\n[+] All IPs for this domain:")
            for i, ip in enumerate(results['all_ips'], 1):
                print(f"  {i}. {ip}")
        
        # Geographic information
        geo_info = results.get('geo_info')
        if geo_info:
            print(f"\n[+] Geolocation Information:")
            print(f"  Country: {geo_info['country']}")
            print(f"  Region: {geo_info['region']}")
            print(f"  City: {geo_info['city']}")
            print(f"  ISP: {geo_info['isp']}")
            print(f"  Organization: {geo_info['org']}")
            print(f"  Timezone: {geo_info['timezone']}")
            if geo_info['lat'] != 'Unknown' and geo_info['lon'] != 'Unknown':
                print(f"  Coordinates: {geo_info['lat']}, {geo_info['lon']}")

    def ip_finder(self):
        """Main function of IP finder"""
        while True:
            try:
                host_input = input('\n[+] Enter URL/Hostname (or "back" to return): ')
                
                if host_input.lower() == 'back':
                    break
                    
                validated_host, error = self.validate_input(host_input)
                if error:
                    print(f"\033[91m[!] Error: {error}\033[0m")
                    continue
                
                print(f"\n[*] Resolving {validated_host}...")
                
                # Information gathering
                results = {}
                
                # Main IP
                primary_ip = self.get_ip_basic(validated_host)
                if not primary_ip:
                    print(f"\033[91m[!] Could not resolve {validated_host}\033[0m")
                    continue
                    
                results['primary_ip'] = primary_ip
                results['ip_type'] = self.check_ip_type(primary_ip)
                results['all_ips'] = self.get_all_ips(validated_host)
                results['reverse_dns'] = self.reverse_dns_lookup(primary_ip)
                
                # Accessibility check
                print("[*] Checking connectivity...")
                results['is_reachable'] = self.ping_host(primary_ip)
                results['open_ports'] = self.check_port_connectivity(primary_ip)
                
                # Geographic information (for public IPs only)
                if results['ip_type'] == "Public IP":
                    print("[*] Getting geolocation info...")
                    results['geo_info'] = self.get_ip_geolocation(primary_ip)
                
                # Show result
                self.display_results(validated_host, results)
                
            except KeyboardInterrupt:
                print("\n[!] Interrupted by user")
                break
            except Exception as e:
                print(f"\033[91m[!] Error: {e}\033[0m")
            
            input("\nPress Enter to continue...")

def main():
    """Main function"""
    try:
        ip_finder = IPFinder()
        ip_finder.ip_finder_banner()
        ip_finder.ip_finder()
    except KeyboardInterrupt:
        print("\n[!] Program interrupted")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    main()
