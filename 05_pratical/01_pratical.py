# Write a program that takes two lists and 
# returns True if they have at least one common member.

# def common_number(list1, list2):
#     for item in list1:
#         if item in  list2:
#             return True
#     return False

# list1 = [1, 2, 3, 4, 5]
# list2 = [5, 6, 7, 8, 9]

# print(common_mumber(list1, list2))

def common_number(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

print(common_number(list1, list2))
