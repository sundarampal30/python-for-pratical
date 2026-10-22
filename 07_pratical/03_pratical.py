# Write a Python program to read the last n lines of a file.

n = int(input("Enter the number of lines:"))
f = open("sample.txt", "r")
lines = f.readline()

print("Last", n,  "lines are:")
for  line in lines[-n:]:
    print(line, end="")

f.close()    