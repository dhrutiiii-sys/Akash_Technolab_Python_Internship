def show(**num):
    print(num.items())

show(n1=10)
show(n1=10,n2=20)
show(n1=10,n2=20,n3=30)


def showw(**num):
    for i,j in num.items():
        print(i,j)

showw(n1=10,n2=20)


def shoow(**num):
    sum = 0
    for i,j in num.items():
        sum = sum +j
        print("Sum is",sum)

shoow(n1=10,n2=20)