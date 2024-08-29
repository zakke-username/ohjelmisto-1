gender = input("Anna sukupuoli (MIES/NAINEN): ")
hemoglobin = float(input("Anna hemoglobiiniarvo: "))

if gender == "MIES":
    if hemoglobin < 134:
        print("Arvo on alhainen.")
    elif hemoglobin > 195:
        print("Arvo on korkea.")
    else:
        print("Arvo on normaali.")
elif gender == "NAINEN":
    if hemoglobin < 117:
        print("Arvo on alhainen.")
    elif hemoglobin > 175:
        print("Arvo on korkea.")
    else:
        print("Arvo on normaali.")