# While loop- runs till the given condition is true

x=input('\nenter Your phone number: ')

while not len(x)==10:
    print("Phone number must contain 10 digits.")
    print(f"you number contain only {len(x)} digits.")
    x=input('enter the phone number:\n')
print('entered phone no. is correct.')
