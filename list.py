# Creating a list

my_list = []

# appending values to the list

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("my_list:", my_list)

# adding a value at second position

my_list.insert(1, 15)

print("Edited my_list:", my_list)

# creating another list

my_list2 = [50, 60, 70]
print(my_list2)

my_list.extend(my_list2)
print("Extended my_list:",  my_list)

# Removing an element from my_list
my_list.pop()

print(my_list)

# Sorting my_list in ascending order
my_list.sort()

print("Sorted List:", my_list)

print(my_list[3])
