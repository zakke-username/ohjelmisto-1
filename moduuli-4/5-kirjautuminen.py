username = "python"
password = "rules"
username_input = ""
password_input = ""

attempts = 0
while attempts < 5:
    username_input = input("Käyttäjätunnus: ")
    password_input = input("Salasana: ")

    if username_input == username and password_input == password:
        print("Tervetuloa!")
    else:
        print("Pääsy evätty")
        attempts += 1
