limit = int(input("Enter limit: "))
innerSpace = 0
x = int((limit-1)/2)

print("*"*limit)

for i in range(x,0,-1):
    print("*"*i," "*innerSpace,"*"*i)
    innerSpace = innerSpace + 2