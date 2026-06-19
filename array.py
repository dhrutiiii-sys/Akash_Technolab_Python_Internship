import array as arr

arrdata = arr.array("i",[20,10,99,74,56,36])
print("First Value is",arrdata[1])


from array import *

arrdata = array("i",[20,10,99,74,56,36])
print("First Value is",arrdata[1])


from array import *

arrdatta = array("i",[20,10,99,74,56,36])

for i in arrdatta:
    print(i)

print(arrdatta[1:3])
print(arrdatta[3:])
print(arrdatta[:])

arrdatta[1] = 25
print(arrdatta[1])


from array import *

arrdata1 = array("i",[20,10,99,74,56])
arrdata2 = array("i",[28,9,5,66,7,10])

myarr = arrdata1 + arrdata2
print(myarr)



#Array Methods

#Append - add an element at the end of data

import array as arr

array_ele = arr.array("i",[10,20,30,40,50])

array_ele.append(45)
print(array_ele)



#Count

import array as arr

array_elle = arr.array("i",[10,20,30,40,50])

x = array_elle.count(10)
print(x)



#Extend add whole new list

import array as arr

arrayy_ele = arr.array("i",[10,20,30,40,50])
arrayy_ele2 = arr.array("i",[25,35,55])

arrayy_ele.extend(arrayy_ele2)
print(arrayy_ele)


#Index - Return the index of the element

import array as arr

arraay = arr.array("i",[10,20,30,40,50])
x = arraay.index(10)
print(x)

arraay.insert(3,15)
print(arraay)


#Pop()- remove the element at the specified position

arraay.pop(1)
print(arraay)


#remove - Remove the first item with the specified value

arraay.remove(30)
print(arraay)


#reverse

arraay.reverse()

print(arraay)

#len

count = len(arraay)
print(count)



#input from user

import array as a1

arr_ele = a1.array("i",[])
n = int(input("Enter no of element :"))

for i in range(n):
    n1 = int(input("Enter value:"))
    arr_ele.append(n1)

    print(arr_ele)
    print(type(arr_ele))