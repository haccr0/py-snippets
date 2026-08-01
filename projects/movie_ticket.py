import sys

# collecting data
user_age_q = input("what is your age?")
user_id_q = input("do you have id? YES/NO: ")

# checking if age is a number
if not user_age_q.isdigit():
    sys.exit("type a valid number for age, eg: 18")

user_age = int(user_age_q)
user_id = user_id_q.upper()

# user id boolean
if user_id == "YES":
    user_id = True
elif user_id == "NO":
    user_id = False
# check whether user input is valid
else:
    sys.exit("Invalid input for ID question, Please enter YES or NO")

# useful statements
sorry = "sorry!"
thanks = "thank you!"

# checking requirements
if user_age >= 18 and user_id:
    print(f"{thanks.upper()}, you can enter")
elif user_age >= 18 and not user_id:
    print(f"{sorry.upper()}, you need an id to enter")
else:
    print(f"{sorry.upper()}, you are too young to enter")
