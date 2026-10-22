# Define a function that computes the length of a given list or string.

# def length(data):
#     count = 0
#     for item in data:
#         count += 1
#         return count

# print(length([1, 2, 3, 4]))  # 4
# print(length("hello")) # 5    

def length(data):
    count = 0 
    for item in data:
        count += 1
        return count

print(length([1, 2, 3, 4,])) # 4
print(length("Hello")) # 5    