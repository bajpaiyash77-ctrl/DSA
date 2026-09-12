num = int(input("Enter a number: "))

a = 0
b = 1
found = False

while a <= num:
    if a == num:
        found = True
        break

    c = a + b
    a = b
    b = c

if found:
    print("Fibonacci Number")
else:
    print("Not a Fibonacci Number")