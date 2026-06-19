mylist = []

no = int(input("Enter number of elements"))

for i in range(0,no):

    myvalue = input("Enter value")

    mylist.append(myvalue)

print(mylist)

mytuple = tuple(mylist)
print(mytuple)