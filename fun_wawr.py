def printName(a):
    msg = "Hello" + a
    return msg

print(printName("Dhruti"))


def sum(n1,n2):
    ans = n1 + n2
    return ans

a1 = sum(10,20)
print("Sum is",a1)



def doSum(a,b,c):
    d = a + b + c
    return d

def avg(total):
    per = total/300*100
    return per


totalmarks = doSum(80,90,70)
print("Total Marks is",totalmarks)


getper = avg(totalmarks)
print("% is",getper)
    