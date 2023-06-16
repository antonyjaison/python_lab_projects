def rev(n):
    if len(n) == 1:
        return n
    else:
        l = len(n)
        return rev(n[l - 1]) + rev(n[:l - 1])

n = input("Enter a string : \n")
print("Reversed sting is : ",rev(n))