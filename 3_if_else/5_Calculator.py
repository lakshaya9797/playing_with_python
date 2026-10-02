import math
add,mult,sub,divi=0,0,0,0

x=float(input('\n\nEnter the First Number: '))
y=float(input('Enter the Second Number:'))

print('\nfor Multiplication-Press M\n'
         'for Division - press D\n'
         'for Addition - press A\n'
         'for Substraction- press S\n')
op=input('Select the Operation: ').lower()


if op=="m":
    mult=x*y
    print(f'Product of the Numbers is {mult}')
elif op=="a":
    add=x+y
    print(f'Addition of the Numbers is {add}')
elif op=="s":
    sub=x-y
    print(f'Substracion of the Numbers is {sub}')
elif op=="d":
    divi=x/y
    print(f'Division of the Numbers is {divi}')
else:
    print('You entered Wrong Charater.')