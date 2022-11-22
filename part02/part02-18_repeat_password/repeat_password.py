password = input("Password: ")

while True:
    if password == input("Repeat password: "):
        print("User account created!")
        break
    print("They do not match!")