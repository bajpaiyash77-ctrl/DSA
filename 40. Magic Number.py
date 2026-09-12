num = int(input("Enter a number: "))

original = num

while num >= 10:
    sum = 0

    while num > 0:
        digit = num % 10
        sum = sum + digit
        num = num // 10

    num = sum

if num == 1:
    print("Magic Number")
else:
    print("Not a Magic Number")