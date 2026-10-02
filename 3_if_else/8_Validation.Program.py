# validate user input excercise
# username is no more than 12 characters
# username must not contain spaces
# username must not contain digits

a=input('Enter you name: ')
if len(a)>12 :
    print("Name can't exceed 12 characters")
elif not a.find(' ')==-1:
    print("Name can't not have Space")
elif not a.isalpha():
    print(' You can not enter numbers.')

else:
    print("Your Name is valid.")

