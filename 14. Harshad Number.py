num = int(input("Enter a number: "))

original = num
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

if original % sum == 0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")