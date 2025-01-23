import os, sys, whois 
from colorama import Fore

def show_whois_banner():
    print(f"""
          _   {Fore.CYAN}v{Fore.WHITE}[1.0]  _         __     {Fore.CYAN} v{Fore.WHITE}[1.0]{Fore.CYAN}      _
__      _| |__   ___ (_)___    / _| ___  ___  _ __ (_)_  __
\ \ /\ / / '_ \ / _ \| / __|  | |_ / _ \/ _ \| '_ \| \ \/ /
 \ V  V /| | | | (_) | \__ \  |  _|  __/ (_) | | | | |>  <
  \_/\_/ |_| |_|\___/|_|___/  |_|  \___|\___/|_| |_|_/_/\_\\
{Fore.RED}==========================================================={Fore.CYAN}
                      by evilfeonix
                  evilfeonix@gmail.com{Fore.WHITE}
          [+]{Fore.CYAN} Subscribe To Our YouTube Channel{Fore.WHITE} [+] 
{Fore.RED}==========================================================={Fore.WHITE}

    [01] {Fore.CYAN}Get Whois Data{Fore.WHITE}
    [02] {Fore.CYAN}Exit Whois{Fore.WHITE}

    """)

def get_whois_data(domain):
    try:
        w = whois.whois(domain)
        return w
    except Exception as e:
        return f"{Fore.RED}Error: {str(e)}\n{Fore.WHITE}"

if __name__ == "__main__":
    show_whois_banner()
    act = input(f"{Fore.CYAN}>>>>> {Fore.WHITE}[Enter your Choice]{Fore.CYAN} <<<<< {Fore.WHITE}:{Fore.BLUE} ")
    if act in ['1','01']:
        os.system("clear || cls")
        domain = input(f"\n{Fore.CYAN}Enter the domain name {Fore.WHITE}(e.g., example.com):{Fore.BLUE} ")
    elif act in ['2','02']:
        print(f"{Fore.RED}Thanks for Using Whois-Feonix.\n{Fore.WHITE}")
        os.sys.exit()
    else:
        print(f"{Fore.RED}Invalid Choice.\n{Fore.WHITE}")
        os.sys.exit()

    whois_data = get_whois_data(domain)
    print(f"\n{Fore.CYAN}WHOIS Data for", domain)
    print(f"{Fore.BLUE}{whois_data}{Fore.WHITE}")
