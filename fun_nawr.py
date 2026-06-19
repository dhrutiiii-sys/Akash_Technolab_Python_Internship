def sum():
    n1 = 10
    n2 = 20
    ans = n1 + n2
    return ans


ans = sum()
print("Sum is",ans)



def sum1():
    n1 = 10
    n2 = 20
    ans = n1 + n2
    return ans,n1,n2

ans,n1,n2 = sum1()
print("n1 is",n1)
print("n2 is",n2)
print("Sum is",ans)


def myCalc(a,b):
    c = a + b
    d = a - b
    e = a * b
    f = a / b
    return c,d,e,f

ans = myCalc(10,20)
print(ans)

for i in ans :
    print("Ans is",i)

#Best Example

def doSum(a,b):
    ans = a + b
    return ans

def doSub(a,b):
    ans = a - b
    return ans

summ = doSum(20,10)
print("Sum is",summ)

subb = doSub(20,10)
print("Sub is",subb)

#ex 2

a = int(input("Enter No1:"))
b = int(input("Enter No2:"))

def doSumm(a,b):
    ans = a + b
    return ans

def doPercentage(a):
    ans = a/200*100
    return ans

summ1 = doSumm(a,b)
print("Sum is",summ1)

subb1 = doPercentage(summ1)
print("Percentage is",subb1)



