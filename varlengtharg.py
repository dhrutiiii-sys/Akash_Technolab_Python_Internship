def show(*num):
    print(num)

show(10)
show(10,20)
show(10,20,30)



def showw(*num):
    sum = 0
    for i in num:
        sum = sum + i
        print("Sum is",sum)

showw(10,20)
showw(10,20,30)
    