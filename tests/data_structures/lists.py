# lists: like a shopping list (ordered items)
# dictionaries: like a phone book (paired items)
# tuples : like coordinates (fixed value)
# sets : like a bag of unique items

age = 25
has_license = True

my_list = ["alice", age, has_license]

name = my_list[0]
age = my_list[1]
license = my_list[-1]

print(f"my name is {name} and I am {age} years old and I have a license: {license}")

my_list[0] = "bob"
my_list.append('arisu')
my_list.remove(age)

print(my_list)