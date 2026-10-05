# program using a for loop to calculate the factorial of a number (for example, n=5).

fact=1
x=int(input("Enter the Number for Factorial: "))
if x<=0:
    print("You must enter the values greater than 0")
else:    
    for i in range(1,x+1):
        fact=fact*i
    print(fact)
