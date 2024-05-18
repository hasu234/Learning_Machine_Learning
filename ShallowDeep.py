import copy

# create a 2d list having 3 rows and 4 columns

list1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# create a shallow copy of list1

list2 = copy.copy(list1)

# create a deep copy of list1

list3 = copy.deepcopy(list1)

# Update the first element of list1

list1[0][0] = 100

# print the list1

print("list1:", list1)

# print the list2

print("list2:", list2)

# print the list3

print("list3:", list3)
