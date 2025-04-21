import os
from colorama import Fore
import banners

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("\nPress [Enter] to continue...")

def start():
    clear_screen()
    banners.start_banner()

def reload(banner):
    clear_screen()
    if banner == "start":
        banners.start_banner()
    elif banner == "shodan":
        banners.shodan_banner()
    elif banner == "BoganBuster":
        banners.BoganBuster_banner()
    elif banner == "port_scanner":
        banners.port_scanner_banner()
    elif banner == "sql_tester":
        banners.sql_tester_banner()