# Write a function that reverses the user defined value. e. Write a function to check the input value is Armstrong and also write the function for Palindrome.

# def reverse_number(n):
#     rev = 0
#     while n >  0:
#         digit = n % 10
#         rev = rev  * 10 + digit
#         n = n // 10
#     return rev

# num = int(input("Enter a number:"))
# print("Reverse number:", reverse_number(num))      

def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n  = n // 10
        return rev

num = int(input("Enter a number:"))
print("Reverse number:", reverse_number(num))    