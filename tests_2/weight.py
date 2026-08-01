weight = input("your weight please")
unit = input("weight in POUNDS(L) or in KILO(K)")

if unit.upper() in ["L", "POUNDS"]:
    POUNDS = int(weight) * 0.45
    print(POUNDS)

elif unit.upper() in ["K", "KILO"]:
    KILO = int(weight) / 0.45
    print(KILO)

else:
    print("SOMETHING WENT WRONG!! OOPS!!")
