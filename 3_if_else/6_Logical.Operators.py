

# Logical Operators - or, and, not

z= True
if z:           # it will run as long as z contains the Boolean Value " True "
    print("\nProgram to find in which Quadrant the given Angle lies .")
    x=int(input('Enter the Angle Value: '))
    if x<=90 and x>=0:
        print("\nEntered Number lied in 1st Quadrant")
    elif x>90 and x<=180:
        print("Entered Number is in 2nd Quadrant.")
    elif x<=270 and x>180:
        print("Entered Number is in 3rd Quadrant.")
    elif x>=270 and x<360:
        print("Entered Number is in 4th Quadrant.")
    elif x<0 or x> 360:
        print("Entered number must be between 0-360")
