username = "python"
password = "rules"

attempts = 0
while attempts < 5:
    username_input = input("Käyttäjätunnus: ")
    password_input = input("Salasana: ")

    if username_input == username and password_input == password:
        print("Tervetuloa!")
        break
    else:
        print("Pääsy evätty")
        attempts += 1
