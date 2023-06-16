# Antony Jaison
# PKD21IT019
# linear search

n = int(input("Enter the limit:"))
a = []
count = 0

# input array
for i in range(n):
    x = int(input())
    a.append(x)

num = int(input("Enter the number for search:"))

# search the number
for i in range(n):
    if a[i] == num:
        print("Element found at position", i+1)
        count = count + 1
        break

if count <= 0:
    print("Element not found")