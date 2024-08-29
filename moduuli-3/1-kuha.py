kuha = float(input("Anna kuhan pituus sentteinä: "))

if kuha < 37:
    diff = 37 - kuha
    print(f"Laske kuha takaisin järveen! Se on {diff:.2f} cm liian lyhyt.")
else:
    print("Onneksi olkoon")