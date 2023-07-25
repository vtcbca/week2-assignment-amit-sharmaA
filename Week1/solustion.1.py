# Write a python script to enter any number and check its prime or not.
num = int(input("enter a number: "))
 
for i in range(2, num):
    if num % i  == 0:
        print("not prime number")
        break
else:
    print("IS prime number")
