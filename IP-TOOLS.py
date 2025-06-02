import os
import sys
import time
import random
import platform
from datetime import datetime

# Import modules (make sure they are in the same directory)
try:
    import IP_finder
    import check_whois
    import port_scanner
except ImportError as e:
    print(f"[!] Error importing modules: {e}")
    print("[!] Make sure all required files are in the same directory")
    sys.exit(1)

class IPToolsManager:
    def __init__(self):
        self.version = "3.0"
        self.author = "Amirprx3"
        self.tools = {
            1: {"name": "IP-FINDER", "module": "IP_finder", "description": "Enhanced IP lookup with geolocation"},
            2: {"name": "PORT-SCANNER", "module": "port_scanner", "description": "Fast multi-threaded port scanner"},
            3: {"name": "WHOIS-CHECKER", "module": "check_whois", "description": "Comprehensive WHOIS information"},
            4: {"name": "ABOUT", "module": "about", "description": "About this tool"},
            5: {"name": "EXIT", "module": "exit", "description": "Exit the program"}
        }

    def clear_screen(self):
        """Clear page"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def neonEffect(self, text):
        """Neon effect for text display"""
        neon_colors = [
            "\033[1;37;40m",  # White
        ]
        
        for char in text:
            color = random.choice(neon_colors)
            print(color + char, end="", flush=True)
            time.sleep(0.001)
        print('\033[0m')

    def main_banner(self):
        """Show main banner"""
        banner = f'''
╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                               ║
║          ██╗██████╗       ████████╗ ██████╗  ██████╗ ██╗     ███████╗         ║
║          ██║██╔══██╗      ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝         ║
║          ██║██████╔╝ █████╗  ██║   ██║   ██║██║   ██║██║     ███████╗         ║
║          ██║██╔═══╝  ╚════╝  ██║   ██║   ██║██║   ██║██║     ╚════██║         ║
║          ██║██║              ██║   ╚██████╔╝╚██████╔╝███████╗███████║         ║
║          ╚═╝╚═╝              ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝         ║
║                                                                               ║
║                        Enhanced Network Security Toolkit                      ║
║                                                                               ║
║  Version: {self.version}                                                                 ║
║  Author: {self.author}                                                             ║
║  GitHub: https://github.com/Amirprx3                                          ║
║  OS: {platform.system()} {platform.release()}                                                               ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
        '''
        self.neonEffect(banner)

    def show_system_info(self):
        """Show system information"""
        print(f"\n{'='*60}")
        print(f"{'SYSTEM INFORMATION':^60}")
        print(f"{'='*60}")
        print(f"Platform: {platform.platform()}")
        print(f"Architecture: {platform.architecture()[0]}")
        print(f"Processor: {platform.processor()}")
        print(f"Python Version: {platform.python_version()}")
        print(f"Current Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    def show_menu(self):
        """Show menu"""
        print(f"\n{'='*81}")
        print(f"{'AVAILABLE TOOLS':^81}")
        print(f"{'='*81}")
        
        for key, tool in self.tools.items():
            if key <= 3:  # Main tools
                status = "✓ Available"
                color = "\033[92m"  # Green
            elif key == 4:
                status = "! Information"
                color = "\033[94m"  # Blue
            else:
                status = "✗ Exit"
                color = "\033[91m"  # Red
                
            print(f"{color}{key}) {tool['name']:<15} - {tool['description']:<30} [{status}]\033[0m")

    def loading_animation(self, tool_name):
        """Loading animation"""
        loading_chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        duration = random.randrange(1, 3)
        
        print(f"\n[*] Loading {tool_name}", end='', flush=True)
        
        for i in range(duration * 10):
            char = loading_chars[i % len(loading_chars)]
            print(f"\r[{char}] Loading {tool_name}...", end='', flush=True)
            time.sleep(0.1)
        
        print(f"\r[✓] {tool_name} loaded successfully!" + " " * 20)
        time.sleep(0.5)

    def show_about(self):
        """Display information about the tool"""
        about_text = f'''
╔═══════════════════════════════════════════════════════════════════════════════╗
║                              ABOUT IP-TOOLS v{self.version}                              ║
╠═══════════════════════════════════════════════════════════════════════════════╣
║                                                                               ║
║  This is an enhanced network security toolkit that provides various           ║
║  network reconnaissance and analysis tools.                                   ║
║                                                                               ║
║  [+] FEATURES:                                                                ║
║   • Enhanced IP Finder with geolocation                                       ║
║   • High-speed multi-threaded port scanner                                    ║
║   • Comprehensive WHOIS information checker                                   ║
║   • Improved error handling and user experience                               ║
║   • Cross-platform compatibility                                              ║
║                                                                               ║
║  [+] IMPROVEMENTS IN v{self.version}:                                                    ║
║   • Faster port scanning with optimized threading                             ║
║   • Better input validation and error handling                                ║
║   • Enhanced output formatting and colors                                     ║
║   • Added geolocation information for IP addresses                            ║
║   • Improved WHOIS data parsing and display                                   ║
║   • Added progress indicators and loading animations                          ║
║                                                                               ║
║  [+] CONTACT:                                                                 ║
║   GitHub: https://github.com/Amirprx3                                         ║
║   Original Author: Amirprx3                                                   ║
║   Enhanced Version: {datetime.now().year}                                                      ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
        '''
        print(about_text)

    def handle_tool_selection(self, choice):
        """Tool selection management"""
        if choice == 1:  # IP Finder
            self.loading_animation("IP Finder")
            self.clear_screen()
            try:
                ip_finder = IP_finder.IPFinder()
                ip_finder.ip_finder_banner()
                ip_finder.ip_finder()
            except Exception as e:
                print(f"\033[91m[!] Error running IP Finder: {e}\033[0m")
                
        elif choice == 2:  # Port Scanner
            self.loading_animation("Port Scanner")
            self.clear_screen()
            try:
                scanner = port_scanner.PortScanner()
                scanner.run_interactive()
            except Exception as e:
                print(f"\033[91m[!] Error running Port Scanner: {e}\033[0m")
                
        elif choice == 3:  # WHOIS Checker
            self.loading_animation("WHOIS Checker")
            self.clear_screen()
            try:
                whois_checker = check_whois.WHOISChecker()
                whois_checker.check_whois_banner()
                whois_checker.main()
            except Exception as e:
                print(f"\033[91m[!] Error running WHOIS Checker: {e}\033[0m")
            
        elif choice == 4:  # About
            self.clear_screen()
            self.show_about()
            self.show_system_info()
            input("\nPress Enter to continue...")
            
        elif choice == 5:  # Exit
            print("\n\033[92m[+] Thank you for using IP-TOOLS!\033[0m")
            print("\033[92m[+] Stay safe and happy hacking! \033[0m")
            sys.exit(0)
            
        else:
            print(f"\033[91m[!] Invalid choice: {choice}\033[0m")
            print("\033[93m[!] Please select a number between 1-6\033[0m")

    def check_dependencies(self):
        """Check dependencies"""
        required_modules = ['socket', 'whois', 'requests', 'threading']
        missing_modules = []
        
        for module in required_modules:
            try:
                __import__(module)
            except ImportError:
                missing_modules.append(module)
        
        if missing_modules:
            print(f"\033[91m[!] Missing required modules: {', '.join(missing_modules)}\033[0m")
            print("\033[93m[!] Please install missing modules using pip:\033[0m")
            for module in missing_modules:
                print(f"  pip install {module}")
            return False
        return True

    def run(self):
        """Main program execution"""
        # Check dependencies
        if not self.check_dependencies():
            sys.exit(1)
            
        print("\033[92m[+] All dependencies satisfied!\033[0m")
        time.sleep(1)
        
        while True:
            try:
                self.clear_screen()
                self.main_banner()
                self.show_menu()
                
                choice = input(f"\n\033[96m[+] Please select a tool (1-{len(self.tools)}): \033[0m").strip()
                
                if not choice:
                    print("\033[91m[!] Please enter a valid number\033[0m")
                    time.sleep(1)
                    continue
                
                try:
                    choice_num = int(choice)
                    if choice_num in self.tools:
                        self.handle_tool_selection(choice_num)
                    else:
                        print(f"\033[91m[!] Please enter a number between 1-{len(self.tools)}\033[0m")
                        time.sleep(1)
                except ValueError:
                    print("\033[91m[!] Please enter a valid number\033[0m")
                    time.sleep(1)
                    
            except KeyboardInterrupt:
                print("\n\n\033[93m[!] Program interrupted by user\033[0m")
                print("\033[92m[+] Goodbye! \033[0m")
                sys.exit(0)
            except Exception as e:
                print(f"\033[91m[!] Unexpected error: {e}\033[0m")
                input("Press Enter to continue...")

def main():
    """Main entry point"""
    try:
        # Check Python version
        if sys.version_info < (3, 6):
            print("\033[91m[!] Python 3.6 or higher is required!\033[0m")
            sys.exit(1)
            
        # Create and run the tool manager
        manager = IPToolsManager()
        manager.run()
        
    except KeyboardInterrupt:
        print("\n\033[93m[!] Program interrupted\033[0m")
        sys.exit(0)
    except Exception as e:
        print(f"\033[91m[!] Fatal error: {e}\033[0m")
        sys.exit(1)

if __name__ == "__main__":
    main()
