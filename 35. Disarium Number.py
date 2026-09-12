num = int(input("Enter a number: "))

original = num
digits = len(str(num))
sum = 0
position = digits

while num > 0:
    digit = num % 10
    sum = sum + digit ** position
    position = position - 1
    num = num // 10

if sum == original:
    print("Disarium Number")
else:
    print("Not a Disarium Number")