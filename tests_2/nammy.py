name = input('What is your name?')

if len(name) < 3:
    print("name should be more than 3 characters")

elif len(name) > 10:
    print("name should be les than 10 characters")

else:
    print('GOOD NAME!!!!!!')