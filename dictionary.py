mydic = {'A':'Akash',1:'One',9:9,'Z':99,'B':'B'}

print(mydic)
print(mydic['A'])
print(mydic[1])

mydic['A'] = "Apple"
print(mydic)



my_dicti = {1: 'Mango',2: 'Apple', 3: 'Kiwi', 4: 'Cherry,chiku'}

for x in my_dicti:

    print("Key is",x,"Value is",my_dicti[x])

for x in my_dicti.items():
    print(x)


for x in my_dicti.keys():
    print(x)


for x in my_dicti.values():
    print(x)


