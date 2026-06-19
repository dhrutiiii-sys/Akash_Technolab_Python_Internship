mylist1 = ["Java","Python","Angular","React"]
mylist2 = [99,58,6,72,36,96]

mylist1.sort()
print(mylist1)


mylist2.sort()
print(mylist2)
mylist2.reverse()
print(mylist2)

mylist1.reverse()
print(mylist1)


mylist = [99,20,38,10,80]
print(sorted(mylist))
print(sorted(mylist,reverse=True))


mylistt = [99,20,38,10,80]

print(max(mylistt))
print(min(mylistt))
print(sum(mylistt))


myylist = ["java","Python",10,"Angular",99,"Python"]
mycount = myylist.count("Python")
print(mycount)
myylist.append("React")
print(myylist)

myylist.insert(2,"Django")
print(myylist)

position = myylist.index("java")
print(position)

myylist.pop(1)
print(myylist)

myylist.remove("Python")
print(myylist)


myylist.clear()
print(myylist)


myliist = ["c","Python",88,"Java"]
print(myliist)

mynewlist = myliist.copy()
print(mynewlist)

myliist.extend(mynewlist)
print(myliist)


