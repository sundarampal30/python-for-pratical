# Write a Python program to print a specified list 
# after removing the 0th, 2nd, 4th and 5th elements

my_list = ['Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Black']

result = [x for i, x in enumerate(my_list) if i not in(0, 2, 4, 5)]
print("Original List:", my_list)
print("aftrt Removing Element:", result)
