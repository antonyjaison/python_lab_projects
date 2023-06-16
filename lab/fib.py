def fib(n):
    a = 0
    b = 1
    c = 0
    if n == 1:
        print(a)
    elif n == 2:
        print(a)
        print(b)
    else:
        print(a)
        print(b)
        for i in range(n - 1):
            c = a + b
            print(c)
            a = b
            b = c


num = int(input("Enter a number : "))
fib(num)
