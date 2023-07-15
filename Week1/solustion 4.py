# Python program to check if the number is an Armstrong number or not

b = int(input("Enter a number: "))
sum = 0
temp = b
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if b == sum:
   print(b,"is an Armstrong number")
else:
   print(b,"is not an Armstrong number")
