mydic = {}
no = int(input("Enter no:"))

for i in range(no):
    k,v = input("Enter key value").split()
    mydic[k] = [v]
print(mydic)


mydic = {}
count = int(input("How many records:"))

for i in range(0,count):
    mykey = input("Enter key ")
    mydic[mykey] = input("Enter value")
print(mydic)