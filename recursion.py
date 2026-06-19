def countNumber(x):
    if x<10:
        x = x+1
        print(x)
        countNumber(x)

countNumber(0)