import whois
import sys
import os
import time
import json
from datetime import datetime, timedelta
import re

class WHOISChecker:
    def __init__(self):
        self.important_keys = [
            "domain_name", "creation_date", "expiration_date", "updated_date",
            "status", "registrar", "name_servers", "emails", "owner",
            "registrant", "admin", "tech", "billing", "org", "country"
        ]
        
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

    def check_whois_banner(self):
        self.pulseEffect(
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

Enhanced WHOIS Checker v3.0
made by: Amirprx3 (Enhanced)
github: https://github.com/Amirprx3  
            '''
        )

    def validate_domain(self, domain):
        """Domain validation"""
        # Delete protocol
        domain = re.sub(r'^https?://', '', domain)
        # Delete www
        domain = re.sub(r'^www\.', '', domain)
        # Delete path
        domain = domain.split('/')[0]
        
        # Check the domain format
        domain_pattern = r'^[a-zA-Z0-9][a-zA-Z0-9-]{0,61}[a-zA-Z0-9]?\.[a-zA-Z]{2,}$'
        if not re.match(domain_pattern, domain):
            return None, "Invalid domain format"
            
        return domain.lower(), None

    def check_whois(self, domain):
        """Get WHOIS information"""
        try:
            print(f"[*] Querying WHOIS for {domain}...")
            w = whois.whois(domain)
            if not w:
                return None, "No WHOIS data found"
            return w, None
        except Exception as e:
            return None, f"Error occurred: {str(e)}"

    def format_date(self, date_obj):
        """Formatting the date"""
        if not date_obj:
            return "N/A"
            
        if isinstance(date_obj, list):
            date_obj = date_obj[0] if date_obj else None
            
        if isinstance(date_obj, datetime):
            return date_obj.strftime("%Y-%m-%d %H:%M:%S")
            
        return str(date_obj)

    def calculate_domain_age(self, creation_date):
        """Calculate domain age"""
        if not creation_date:
            return "Unknown"
            
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
            
        if isinstance(creation_date, datetime):
            age = datetime.now() - creation_date
            years = age.days // 365
            months = (age.days % 365) // 30
            return f"{years} years, {months} months"
            
        return "Unknown"

    def calculate_expiry_status(self, expiration_date):
        """Calculating Expiration Status"""
        if not expiration_date:
            return "Unknown", "gray"
            
        if isinstance(expiration_date, list):
            expiration_date = expiration_date[0]
            
        if isinstance(expiration_date, datetime):
            now = datetime.now()
            days_left = (expiration_date - now).days
            
            if days_left < 0:
                return f"Expired {abs(days_left)} days ago", "red"
            elif days_left <= 30:
                return f"Expires in {days_left} days (Critical!)", "red"
            elif days_left <= 90:
                return f"Expires in {days_left} days (Warning)", "yellow"
            else:
                return f"Expires in {days_left} days", "green"
                
        return "Unknown", "gray"

    def extract_emails(self, whois_data):
        """Extract emails from WHOIS data"""
        emails = set()
        
        # Check the direct emails field
        if hasattr(whois_data, 'emails') and whois_data.emails:
            if isinstance(whois_data.emails, list):
                emails.update(whois_data.emails)
            else:
                emails.add(whois_data.emails)
        
        # Search in other fields
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        
        for key, value in whois_data.items():
            if value and isinstance(value, str):
                found_emails = re.findall(email_pattern, value)
                emails.update(found_emails)
        
        return list(emails)

    def get_name_servers(self, whois_data):
        """Get name servers"""
        name_servers = []
        
        if hasattr(whois_data, 'name_servers') and whois_data.name_servers:
            if isinstance(whois_data.name_servers, list):
                name_servers = [ns.lower() for ns in whois_data.name_servers if ns]
            else:
                name_servers = [whois_data.name_servers.lower()]
        
        return name_servers

    def analyze_registrar(self, registrar):
        """Registrar analysis"""
        if not registrar:
            return "Unknown"
            
        popular_registrars = {
            'godaddy': 'GoDaddy (Popular)',
            'namecheap': 'Namecheap (Popular)',
            'cloudflare': 'Cloudflare (Popular)',
            'google': 'Google Domains (Popular)',
            'amazon': 'Amazon Route 53 (Cloud)',
            'network solutions': 'Network Solutions (Legacy)'
        }
        
        registrar_lower = registrar.lower()
        for key, description in popular_registrars.items():
            if key in registrar_lower:
                return description
                
        return registrar

    def filter_important_info(self, whois_data):
        """Filtering out important information"""
        important_info = {}
        
        # Main information
        if hasattr(whois_data, 'domain_name'):
            important_info['Domain Name'] = whois_data.domain_name
            
        if hasattr(whois_data, 'registrar'):
            important_info['Registrar'] = self.analyze_registrar(whois_data.registrar)
            
        # Datas
        if hasattr(whois_data, 'creation_date'):
            important_info['Creation Date'] = self.format_date(whois_data.creation_date)
            important_info['Domain Age'] = self.calculate_domain_age(whois_data.creation_date)
            
        if hasattr(whois_data, 'expiration_date'):
            important_info['Expiration Date'] = self.format_date(whois_data.expiration_date)
            expiry_status, color = self.calculate_expiry_status(whois_data.expiration_date)
            important_info['Expiry Status'] = (expiry_status, color)
            
        if hasattr(whois_data, 'updated_date'):
            important_info['Last Updated'] = self.format_date(whois_data.updated_date)
            
        # Domain status
        if hasattr(whois_data, 'status'):
            status = whois_data.status
            if isinstance(status, list):
                important_info['Status'] = ', '.join(status)
            else:
                important_info['Status'] = status
                
        # Name servers
        name_servers = self.get_name_servers(whois_data)
        if name_servers:
            important_info['Name Servers'] = name_servers
            
        # Emails
        emails = self.extract_emails(whois_data)
        if emails:
            important_info['Contact Emails'] = emails
            
        # Owner information
        owner_fields = ['registrant', 'owner', 'org']
        for field in owner_fields:
            if hasattr(whois_data, field):
                value = getattr(whois_data, field)
                if value:
                    important_info['Owner/Organization'] = value
                    break
                    
        # Country
        if hasattr(whois_data, 'country'):
            important_info['Country'] = whois_data.country
            
        return important_info

    def display_important_info(self, important_info):
        """Display important information beautifully"""
        print(f"\n{'='*70}")
        print(f"{'IMPORTANT WHOIS INFORMATION':^70}")
        print(f"{'='*70}")
        
        for key, value in important_info.items():
            if key == 'Expiry Status' and isinstance(value, tuple):
                status, color = value
                color_codes = {
                    'red': '\033[91m',
                    'yellow': '\033[93m', 
                    'green': '\033[92m',
                    'gray': '\033[90m'
                }
                print(f"{key:.<25} {color_codes.get(color, '')}{status}\033[0m")
            elif isinstance(value, list):
                print(f"{key:.<25} {len(value)} items")
                for i, item in enumerate(value, 1):
                    print(f"{'':.<25}   {i}. {item}")
            else:
                print(f"{key:.<25} {value}")

    def display_raw_data(self, whois_data):
        """Raw data display"""
        print(f"\n{'='*70}")
        print(f"{'RAW WHOIS DATA':^70}")
        print(f"{'='*70}")
        
        # Convert to dictionary for better display
        data_dict = {}
        for key in dir(whois_data):
            if not key.startswith('_'):
                value = getattr(whois_data, key)
                if value and not callable(value):
                    data_dict[key] = value
        
        for key, value in sorted(data_dict.items()):
            if isinstance(value, list):
                print(f"\n{key.upper()}:")
                for item in value:
                    print(f"  - {item}")
            elif isinstance(value, datetime):
                print(f"{key.upper()}: {value.strftime('%Y-%m-%d %H:%M:%S')}")
            else:
                print(f"{key.upper()}: {value}")

    def save_to_file(self, domain, whois_data, important_info):
        """Save information to file"""
        try:
            filename = f"whois_{domain.replace('.', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"WHOIS Information for: {domain}\n")
                f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("="*60 + "\n\n")
                
                f.write("IMPORTANT INFORMATION:\n")
                f.write("-"*30 + "\n")
                for key, value in important_info.items():
                    if key == 'Expiry Status' and isinstance(value, tuple):
                        f.write(f"{key}: {value[0]}\n")
                    elif isinstance(value, list):
                        f.write(f"{key}:\n")
                        for item in value:
                            f.write(f"  - {item}\n")
                    else:
                        f.write(f"{key}: {value}\n")
                
                f.write(f"\n{'='*60}\n")
                f.write("RAW WHOIS DATA:\n")
                f.write("-"*30 + "\n")
                f.write(str(whois_data))
                
            print(f"\n\033[92m[+] Data saved to: {filename}\033[0m")
            
        except Exception as e:
            print(f"\033[91m[!] Error saving file: {e}\033[0m")

    def main(self):
        """Main Function"""
        while True:
            try:
                domain_input = input("\n[+] Enter domain name (or 'back' to return): ").strip()
                
                if domain_input.lower() == 'back':
                    break
                    
                if not domain_input:
                    print("\033[91m[!] Domain name cannot be empty\033[0m")
                    continue
                
                # Domain validation
                domain, error = self.validate_domain(domain_input)
                if error:
                    print(f"\033[91m[!] {error}\033[0m")
                    continue
                
                # Select display type
                print(f"\nDisplay options for {domain}:")
                print("1) Important information only")
                print("2) Raw WHOIS data")
                print("3) Both important and raw data")
                print("4) Save to file")
                
                try:
                    choice = int(input("\n[+] Select option (1-4): "))
                except ValueError:
                    print("\033[91m[!] Invalid choice\033[0m")
                    continue
                
                # Get WHOIS information
                whois_data, error = self.check_whois(domain)
                if error:
                    print(f"\033[91m[!] {error}\033[0m")
                    continue
                
                # Information processing
                important_info = self.filter_important_info(whois_data)
                
                # Display based on user selection
                if choice == 1:
                    if important_info:
                        self.display_important_info(important_info)
                    else:
                        print("\033[93m[!] No important information found\033[0m")
                        
                elif choice == 2:
                    self.display_raw_data(whois_data)
                    
                elif choice == 3:
                    if important_info:
                        self.display_important_info(important_info)
                    self.display_raw_data(whois_data)
                    
                elif choice == 4:
                    if important_info:
                        self.display_important_info(important_info)
                        self.save_to_file(domain, whois_data, important_info)
                    else:
                        print("\033[93m[!] No data to save\033[0m")
                else:
                    print("\033[91m[!] Invalid choice\033[0m")
                    continue
                
            except KeyboardInterrupt:
                print("\n[!] Interrupted by user")
                break
            except Exception as e:
                print(f"\033[91m[!] Unexpected error: {e}\033[0m")
            
            input("\nPress Enter to continue...")

def main():
    """Main entry point"""
    try:
        whois_checker = WHOISChecker()
        whois_checker.check_whois_banner()
        whois_checker.main()
    except KeyboardInterrupt:
        print("\n[!] Program interrupted")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    main()
