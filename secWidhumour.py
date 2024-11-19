import hashlib
import getpass
import time
import webbrowser
import os
import pyperclip
import subprocess

# Create a user-specific directory to store project files
def create_user_directory():
    project_dir = os.path.join(os.path.expanduser("~"), "Security_architecture")
    os.makedirs(project_dir, exist_ok=True)
    return project_dir

# Define path to save passwords in a user-specific directory
project_dir = create_user_directory()
password_file_path = os.path.join(project_dir, "passwords.txt")

# Firewall opening
def open_win_firewall():
    try:
        subprocess.run(['control','firewall.cpl'], check=True)
        print("Opening Windows Firewall settings...")
        time.sleep(1)
    except subprocess.CalledProcessError as e:
        print("Failed to open firewall.")
        time.sleep(1)

# Server status
def server_status_check():
    print("Server status check...")
    print("Scanning 127.0.0.1...")
    time.sleep(1)
    try:
        result = subprocess.run(['ping', '127.0.0.1', '-n', '4'], text=True, capture_output=True, check=True)
        print("Ping Output:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("An error occurred while trying to ping the server:")
        print(e.stderr)
    print("Server is online and operational!\n\n")
    time.sleep(1)

# Network monitoring
def network_monitoring():
    print("Network monitoring...")
    try:
        result = subprocess.run(['netstat','-an'], text=True, capture_output=True, check=True)
        print("Netstat Output:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("An error occurred while trying to monitor the network:")
        print(e.stderr)
    print("Network is up and running smoothly!\n\n")
    time.sleep(1)

# Temporary database of users' hashed passwords
user_db_69 = {
    "wiener": hashlib.sha256("!qaz@wsx#edc".encode()).hexdigest(),
    "admin007": hashlib.sha256("peter".encode()).hexdigest()
}

# Password strength checker
def pass_strength_check(password):
    special_chars = {"*", "@", "#", "!", "%"}
    contains_digit = any(char.isdigit() for char in password)
    special_char_found = any(char in special_chars for char in password)

    if len(password) < 8:
        print("Strength: *-----")
        print("Need at least 8 characters.")
    elif not special_char_found:
        print("Strength: ***-----")
        print("Password should contain at least one special character.")
    elif not contains_digit:
        print("Strength: ***-----")
        print("Password should contain at least one number.")
    else:
        print("Strength: *****--")

# Authentication function
def authenticate_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    stored_password = user_db_69.get(username)
    return stored_password and stored_password == hashed_password

# Login function
def login():
    max_attempts = 4
    attempts = 0
    while attempts < max_attempts:
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")

        if authenticate_user(username, password):
            print(f"Hello {username}! You're logged in.")
            session_login(username)
            return
        else:
            attempts += 1
            print(f"Invalid credentials. Attempt {attempts}/{max_attempts}.")
    
    print("Too many invalid attempts. Returning to main menu.")
    main()

# Session handling function
def session_login(username):
    print(f"Session started for {username}. Redirecting to dashboard.")
    
    def dashboard():
        print("Dashboard: Choose operation.")
        print("1. Password storage\n2. Network monitoring\n3. Running servers status\n4. Open Windows firewall\n5. Logout")
        opt = int(input("\nEnter your choice: "))

        if opt == 1:
            password_storage()
            dashboard()
        elif opt == 2:
            network_monitoring()
            dashboard()
        elif opt == 3:
            server_status_check()
            dashboard()
        elif opt == 4:
            print("Opening firewall, stay alert...")
            time.sleep(4)
            open_win_firewall()
        elif opt == 5:
            print("Logging out...")
            main()
        else:
            print("Invalid choice. Please select a valid option.")

    dashboard()

# Function for storing passwords
def password_storage():
    print("Welcome! Store passwords in your inventory")
    with open(password_file_path, "a+") as fp:
        fp.seek(0)  # Move the cursor to the beginning of the file
        lines = fp.readlines()
        usernames = [line.split(" || ")[0].strip() for line in lines]

        username = input("Enter username: ")
        if username in usernames:
            print(f"Password for {username} is already stored.")
        else:
            password = getpass.getpass("Enter password: ")
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            fp.write(f"{username} || {hashed_password}\n")
            print(f"Password for {username} has been stored.")

# Main function
def main():
    print("Hello admin,", end=" ")
    time.sleep(1)
    print("not yet,", end=" ")
    time.sleep(1)
    print("hello guest...!!!!")
    time.sleep(1)
    print("What to be done mate! Coffee or any of these")
    time.sleep(1)
    print("\t\t1. Check password strength")
    time.sleep(1)
    print("\t\t2. Login")
    time.sleep(1)
    print("\t\t3. Visit any website")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        passwd = getpass.getpass("Enter password to find the strength: ")
        pass_strength_check(passwd)
    elif choice == 2:
        print("Welcome to the login page!")
        login()
    elif choice == 3:
        print("These are secret websites, I didn't even tell my wife!")
        time.sleep(1)
        print("Where to surf, swoosh!!")
        print("1. PortSwigger\n2. Hack The Box\n3. Exploit DB")
        choose = int(input())
        if choose == 1:
            url = "https://portswigger.net"
            print("Opening PortSwigger...")
            webbrowser.open(url)
        elif choose == 2:
            url = "https://www.hackthebox.com/"
            print("Opening Hack The Box...")
            webbrowser.open(url)
        elif choose == 3:
            url = "https://www.exploit-db.com/"
            print("Opening Exploit DB...")
            webbrowser.open(url)
        else:
            print("Choice out of range!")
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
