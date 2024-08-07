import hashlib
import getpass
import time
import webbrowser
import os
import pyperclip
import subprocess

                                       # special operations 
# bitdefender opening
def open_win_firewall():
    try:
        subprocess.run(['control','firewall.cpl'],check=True)
        print("opening windows firewall settings...")
        time.sleep(1)
    
    except subprocess.CalledProcessError as e:
        print("failed to open firewall ")
        time.sleep(1)

# server status    
def server_status_check():
    print("Server status check...")
    # Placeholder for actual server status checking logic
    print("scanning 127.0.0.1..")
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
    


    # network monitoring
def network_monitoring():
    print("Network monitoring...")
    try:
        result = subprocess.run(['netstat','-an'], text=True, capture_output=True, check=True)
        print("Netstat Output:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("An error occurred while trying to get network status on  the server:")
        print(e.stderr)

    print("Network is up and running smoothly!\n\n")
    time.sleep(1)
   



# Temporary database of users hashed passwords , not a good practice just for prototype
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
        print("Need something bigger than a Boeing 747!")
        print("Need at least 8 characters")
    elif not special_char_found:
        print("What! Seriously! Even my grandma could guess that password.")
        print("Strength: ***-----")
        print("Password should contain at least one special character.")
    elif not contains_digit:
        print("Your password needs some numbers, like my bank account needs more zeros!")
        print("Strength: ***-----")
    else:
        print("Ready to go! Strong as my biceps")
        print("Strength: *****--")

# Authentication function
def authenticate_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    stored_password = user_db_69.get(username)
    if stored_password and stored_password == hashed_password:
        return True
    return False

# Login function
def login():
    max_attempts = 4
    attempts = 0
    while attempts < max_attempts:
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")

        if authenticate_user(username, password):
            print(f"Hello {username}! You're logged in.")
            # Call session handling function here
            session_login(username)
            return  # Exit function if login is successful
        else:
            attempts += 1
            print(f"Invalid credentials. Attempt {attempts}/{max_attempts}.")
    
    print("Too many invalid attempts. Returning to main menu.")
    main()

# Session handling function
def session_login(username):
    print(f"Session started for {username}. Redirecting to dashboard.")
    
    def dashboard():
        print("Dashboard: Choose operation, warning: I can't hack any agency!")
        print("1. Password storage\n2. Network monitoring\n3. Running servers status\n4.logout")
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
        
        elif opt==4:
            print("logging out: ")
            main()
        else:
            print("Invalid choice. Please select a valid option.")

    dashboard()

# Function for storing passwords
def password_storage():
    print("Welcome! Store passwords in your inventory")
    os.chdir("C:\\Users\\Ravi\\Desktop\\space\\projects\\Security_architecture")
    with open("passwords.txt", "a+") as fp:
        fp.seek(0)  # Move the cursor to the beginning of the file
        lines = fp.readlines()
        usernames = [line.split(" || ")[0].strip() for line in lines]


        username = input("Enter username: ")

        if username in usernames:
            print(f"Password for {username} is already stored in passwords.txt")
           
        else:
            password = getpass.getpass("Enter password: ")
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            fp.write(f"{username} || {hashed_password}\n")
            print(f"Password for {username} has been stored in passwords.txt")
        

# Placeholder function for network monitoring

# Placeholder function for server status checking


# Main function
def main():
    open_win_firewall()
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
    print("\t\t3.visit any website")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        passwd = getpass.getpass("Enter password to find the strength: ")
        pass_strength_check(passwd)
        
    elif choice == 2:
        print("Welcome to the login page!")
        login()
    
    elif choice==3:
        print("these are secret websites ,i didnt even tell my wife!!")
        time.sleep(1)
        print("where to surf, swoosh!!")
        print("1.portswigger\n2.hackthebox\n3.exploitdb")
        choose = int(input())
        if choose==1:
            url = "https://portswigger.net"
            print("opening portswigger.net..")
            time.sleep(1)
            webbrowser.open(url)
        elif choose==2:
            url = "https://www.hackthebox.com/"
            print("opening hackthebox.com..")
            time.sleep(1)
            webbrowser.open(url)
        elif choose==3:
            url = "https://www.exploit-db.com/"
            print("opening exploitdb.com..")
            time.sleep(1)
            webbrowser.open(url)
        else:
            print("choice outraged!!")
        
    else:
        print("Invalid choice. Please select 1 2 3.")




if __name__ == "__main__":
    main()
