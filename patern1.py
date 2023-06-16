limit = int(input("Enter limit: "))
outerSpace = (limit*2)-2
print(" "*outerSpace,"*")
innerSpace = 0
outerSpace = outerSpace - 2

for i in range(2,limit+1):
    print(" "*outerSpace,"*"*i," "*innerSpace,"*"*i)
    outerSpace = outerSpace - 2
    innerSpace = innerSpace + 2


outerSpace = 2
innerSpace = innerSpace - 4
for i in range(limit-1,1,-1):
    print(" "*outerSpace,"*"*i," "*innerSpace,"*"*i)
    innerSpace = innerSpace - 2
    outerSpace = outerSpace + 2
print(" "*outerSpace,"*")
