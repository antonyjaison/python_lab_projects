# Antony Jaison
# PKD21IT019
# matrix multiplication

temp = []
mat1 = []
mat2 = []
mul = []

# function for print list
def printList(r, c, a):
    for i in range(r):
        for j in range(c):
            print(a[i][j], end=" ")
        print()

# input first matrix
r1 = int(input("First matrix row: "))
c1 = int(input("First matrix coloumn: "))
for i in range(r1):
    for j in range(c1):
        x = int(input())
        temp.append(x)
    mat1.append(temp)
    temp = []

# input second matrix
r2 = int(input("Second matrix row: "))
c2 = int(input("Second matrix coloumn: "))
for i in range(r2):
    for j in range(c2):
        x = int(input())
        temp.append(x)
    mat2.append(temp)
    temp = []

# multiplication
if c1 == c2:
    for i in range(r1):
        for j in range(c2):
            s = 0
            for k in range(c2):
                s = s + mat1[i][k] * mat2[k][j]
            temp.append(s)
        mul.append(temp)
        temp = []
    printList(r1, c2, mul)
else:
    print("Multiplication not possible")