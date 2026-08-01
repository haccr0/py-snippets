raining = input("Is it raining? (yes/no): ")
statement = raining.upper()

if statement == "YES":
    raining = True
else:
    raining = False

if not raining:
    print("It's not raining, let's go outside!")
else:
    print("stay where you are!")