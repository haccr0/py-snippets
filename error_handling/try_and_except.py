input = input("Enter a number: ")

try:
    if input > 18:
        print("You are an adult.")
    else:
        print("You are a minor.")
except Exception as e:
    print(f"An error occurred: Please enter a number not letter.")