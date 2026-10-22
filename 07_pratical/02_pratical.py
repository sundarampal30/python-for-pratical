# Write a Python program to append text to a file and display the text.


f = open("sample.txt", "a")
f.write("This is appended text.\n")

f.close()

f = open("sample.txt", "r")
print(f.read())

f.close()

