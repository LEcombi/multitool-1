
# © MultiTool - Made by Yuval Simon | www.bogan.cool
import others
import time
import sys
import Modules.port_scanner as port_scanner
import Modules.BoganBuster as bogan_buster
import Modules.proxy_checker as proxy_checker
import Modules._shodan1 as shodan_searcher
import Modules.exploit_db as vulnerabilities_searcher
import Modules.ddos as ddos_module
import Modules.sql_tester as sql_tester
import Modules.ssh as ssh_bruteforcer

others.start()
# Main Menu Function
def choose_main_option():
    print("\n" + "=" * 30)
    print("Main Menu")
    print("=" * 30)
    print("1️⃣  Reconnaissance")
    print("2️⃣  Attack Tools")
    print("3️⃣  Exit")
    print("=" * 30)
    try:
        return int(input("👉 Please choose an option: "))
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
        time.sleep(1.5)
        return choose_main_option()

# Reconnaissance Menu Function
def choose_recon_option():
    print("\n" + "=" * 30)
    print("Reconnaissance Menu")
    print("=" * 30)
    print("1️⃣  Port Scanner")
    print("2️⃣  BoganBuster (Web Dir Searcher)")
    print("3️⃣  Shodan Searcher")
    print("4️⃣  Vulnerabilities Searcher (Exploit DB)")
    print("5️⃣  Back to Main Menu")
    print("=" * 30)
    try:
        return int(input("👉 Please choose an option: "))
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
        time.sleep(1.5)
        return choose_recon_option()

# Attack Tools Menu Function
def choose_attack_option():
    print("\n" + "=" * 30)
    print("Attack Tools Menu")
    print("=" * 30)
    print("1️⃣  DDOS a Target")
    print("2️⃣  Proxy Checker & Gen")
    print("3️⃣  SQL Injection Tester")
    print("4️⃣  SSH Bruteforcer")
    print("5️⃣  Back to Main Menu")
    print("=" * 30)
    try:
        return int(input("👉 Please choose an option: "))
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
        time.sleep(1.5)
        return choose_attack_option()

# Main Program Loop
while True:
    choice = choose_main_option()
    others.reload("start")
    if choice == 1:  # Reconnaissance"
        while True:
            recon_choice = choose_recon_option()
            if recon_choice == 1:
                port_scanner.scanner().main()
            elif recon_choice == 2:
                bogan_buster.Bogan().main()
            elif recon_choice == 3:
                shodan_searcher.Shodan1().Search()
            elif recon_choice == 4:
                vulnerabilities_searcher.exploit_db_().searcher()
            elif recon_choice == 5:
                break
            else:
                print("❌ Invalid choice. Please try again.")
                time.sleep(1)

    elif choice == 2:  # Attack Tools
        while True:
            attack_choice = choose_attack_option()
            if attack_choice == 1:
                ddos_module.DDOS().start_all()
            elif attack_choice == 2:
                proxy_checker.Proxy_Checker().start()
            elif attack_choice == 3:
                sql_tester.start_sql_()
            elif attack_choice == 4:
                ssh_bruteforcer.Main().start()
            elif attack_choice == 5:
                break
            else:
                print("❌ Invalid choice. Please try again.")
                time.sleep(1)

    elif choice == 3:  # Exit
        print("👋 Exiting the program. Goodbye!")
        sys.exit(0)

    else:
        print("❌ Invalid choice in the main menu. Please try again.")
        time.sleep(1.5)
