# Antony Jaison
# PKD21IT019
# binary search

n = int(input("Enter the limit:"))
a = []
sorted = []
low = 0
high = n - 1
middle = 0

# input array
for i in range(n):
    x = int(input())
    a.append(x)

# sort the array
a.sort()

num = int(input("Enter the number for search:"))

# searching
while low <= high:
    middle = int((low + high) / 2)
    if a[middle] == int(num):
        print("Yes")
        break
    elif (a[middle]) > num:
        high = middle - 1
    else:
        low = middle + 1
if low > high:
    print("No")
