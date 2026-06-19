from array import *

array = array("i",[])
n = int(input("Enter number of elements"))


for i in range(n):
    num = int(input("numbers"))
    array.append(num)


#Ascending order
asc = array[:]
for i in range(n):
    for j in range(i+1,n):
        if asc[i] > asc[j]:
            temp = asc[i]
            asc[i] = asc[j]
            asc[j] = temp
print("Ascending Order:",asc)



#Descending


desc = array[:]
for i in range(n):
    for j in range(i+1,n):
        if desc[i] < desc[j]:
            temp = desc[i]
            desc[i] = desc[j]
            desc[j] = temp
print("Descending Order:",desc)


#Maximum

max_num = array[0]


for i in range(1,n):
    if array[i] > max_num:
        max_num = array[i]

print("Maximum Number:",max_num)

#Minimum

min_num = array[0]

for i in range(1,n):
    if array[i] < min_num:
        min_num = array[i]

print("Minumum Number",min_num)


