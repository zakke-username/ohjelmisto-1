hytti = input("Anna hyttiluokka (LUX/A/B/C): ")

if hytti == "LUX":
    print("Hyttisi on parvekkeellinen hytti yläkannella")
elif hytti == "A":
    print("Hyttisi on ikkunallinen hytti autokannen yläpuolella")
elif hytti == "B":
    print("Hyttisi on ikkunaton hytti autokannen yläpuolella")
elif hytti == "C":
    print("Hyttisi on ikkunaton hytti autokannen alapuolella")
else:
    print("Virheellinen hytti")