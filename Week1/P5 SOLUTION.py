A = input('Enter the string :')
c = 0

A = A.lower()
for i in A:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
    
        c+=1

if c == 0:
    print('No vowels found')
else:
    print('Total vowels are :' + str(c))
