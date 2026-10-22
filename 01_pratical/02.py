# Write a program to generate the Fibonacci series

# n = int(input("Enter the number of  terse:"))

# a, b  = 0,  1
# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

n = int(input("Enter the number of terse:"))

a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b