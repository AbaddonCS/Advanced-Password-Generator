import random
import string
from secrets import choice
import os
from colorama import Fore
import time

def generate_password(length, uppercase=True, lowercase=True, digits=True, special_chars=True):
    chars = ''
    if uppercase:
        chars += string.ascii_uppercase
    if lowercase:
        chars += string.ascii_lowercase
    if digits:
        chars += string.digits
    if special_chars:
        chars += string.punctuation

    if not chars:
        raise ValueError(f"[ {Fore.RED}-{Fore.RESET} ] At least one character type must be selected.")

    password = ''.join(choice(chars) for _ in range(length))
    return password


def save_passwords_to_file(passwords, filename):
    with open(filename, 'w') as file:
        for password in passwords:
            file.write(password + '\n')

def get_boolean_input(prompt):
    while True:
        user_input = input(prompt + " (y/n): ")
        if user_input.lower() == 'y':
            return True
        elif user_input.lower() == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

os.system("clear")
os.system("cls") 
time.sleep(1)
 
banner = f"""
         _nnnn_                      
        dGGGGMMb     ,______________.
       @p~qp~~qMb    | {Fore.MAGENTA}Hey Cutie{Fore.RESET}   |
       M|@||@) M|   _;______________|
       @,----.JM| -'
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMM|   .'
     `-'       `--' ⠀
"""

print(banner)
length = int(input(f"[ {Fore.MAGENTA}+{Fore.RESET} ] Enter the length of your password: "))
uppercase = get_boolean_input(f"[ {Fore.MAGENTA}+{Fore.RESET} ] Include uppercase letters?")
lowercase = get_boolean_input(f"[ {Fore.MAGENTA}+{Fore.RESET} ] Include lowercase letters?")
digits = get_boolean_input(f"[ {Fore.MAGENTA}+{Fore.RESET} ] Include digits?")
special_chars = get_boolean_input(f"[ {Fore.MAGENTA}+{Fore.RESET} ] Include special characters?")
num_passwords = int(input(f"[ {Fore.MAGENTA}+{Fore.RESET} ] How many passwords do you want? "))

passwords = [generate_password(length, uppercase, lowercase, digits, special_chars) for _ in range(num_passwords)]
for password in passwords:
    print(f"[ {Fore.MAGENTA}+{Fore.RESET} ] Generated password:", password)


os.system("clear")
os.system("cls")
filename = input(f"[ {Fore.MAGENTA}+{Fore.RESET} ] Enter a filename to save the passwords (put .txt at the end): ")
if filename:
    save_passwords_to_file(passwords, filename)
    print(f"[ {Fore.MAGENTA}+{Fore.RESET} ] Passwords saved to", filename)

length = 12
uppercase = True
lowercase = True
digits = True
special_chars = True
num_passwords = 5

passwords = [generate_password(length, uppercase, lowercase, digits, special_chars) for _ in range(num_passwords)]
for password in passwords:
    print(f"[ {Fore.MAGENTA}+{Fore.RESET} ] Generated password:", password)

length = 16
uppercase = True
lowercase = False
digits = True
special_chars = False
num_passwords = 3

passwords = [generate_password(length, uppercase, lowercase, digits, special_chars) for _ in range(num_passwords)]
for password in passwords:
    print(f"[ {Fore.MAGENTA}+{Fore.RESET} ] Generated password:", password)

length = 10
uppercase = False
lowercase = True
digits = True
special_chars = False
num_passwords = 2

passwords = [generate_password(length, uppercase, lowercase, digits, special_chars) for _ in range(num_passwords)]
for password in passwords:
    print(f"[ {Fore.MAGENTA}+{Fore.RESET} ] Generated password:", password)



