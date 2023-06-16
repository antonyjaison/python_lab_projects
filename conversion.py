# Antony Jaison
# PKD21IT019
# conversions

num = int(input("Enter the binary number: "))
len = len(str(num))

# binary to decimal
dec = 0
for i in range(len):
    x = (num % 10)
    num = int(num / 10)
    dec = dec + x*(pow(2, i))

print("decimal: ", dec)
a = dec

#decimal to octal
octal = ""
while (dec != 0):
    x = str(dec % 8)
    octal = octal + x
    dec = int(dec / 8)
print("octal: ", octal[::-1])

# decimal to hexadecimal
dec = a
hexa = ""
while dec != 0:
    x = str(dec % 16)

    if int(x) == 10:
        hexa = hexa + "A"
    elif int(x) == 11:
        hexa = hexa + "B"
    elif int(x) == 12:
        hexa = hexa + "C"
    elif int(x) == 13:
        hexa = hexa + "D"
    elif int(x) == 14:
        hexa = hexa + "E"
    elif int(x) == 15:
        hexa = hexa + "F"
    else:
        hexa = hexa + x
    dec = int(dec / 16)
print("hexadecimal: ",hexa[::-1])