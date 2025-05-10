#The system will have stored credentials (username & password).

#The user will be prompted to enter a username and password.

#The program will:

#Check if the input matches the stored credentials.

#Allow 3 attempts before locking the user out.

# --- SIGN-UP PHASE ---
print("📝 Sign-Up")
new_username = input("Create a username: ")
new_password = input("Create a password: ")
print("\n✅ Account created successfully!\n")

# --- LOGIN PHASE ---
print("🔐 Login")
attempts = 3

while attempts > 0:
    print("\nAttempts left:", attempts)
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == new_username and password == new_password:
        print(f"\n✅ Login Successful! Welcome, {username}")
        break
    else:
        attempts -= 1
        print("❌ Incorrect username or password.")
        if attempts == 0:
            print("\n🚫 Too many failed attempts. Account locked.")
