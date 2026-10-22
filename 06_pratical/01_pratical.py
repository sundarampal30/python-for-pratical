#  Write a Python script to sort a dictionary
# by value in ascending and descending order.

# dic = {'a': 50, 'b': 20, 'c': 40, 'd': 10}

# ascending = dict(sorted(dic.items(), key=lambda x: x[1]))
# descending = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))

# print("Ascending order:", ascending)
# print("Descending order:", descending)

dic = {'a': 10,  'b': 20, 'c': 30, 'd': 40}

ascending = dict(sorted(dic.items(), key=lambda x: x[1]))
descending = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))

print("Ascending order:", ascending)
print("Descending order:", descending)