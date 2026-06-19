mydata = {
       1: 10,
       20.5: 100,
       'key': "Hello"
}

print(mydata)
print(type(mydata))
print()

new_list = list(mydata.values())
print(new_list)
print(type(new_list))
print()


new_list2 = tuple(mydata.values())
print(new_list2)
print(type(new_list2))
print()