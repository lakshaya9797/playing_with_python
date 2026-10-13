def myfunction():
    x=10
    y=45    # local variable
    c=x+y
    return c
    
a='hello' # global variable 
b=10    # global variable
d=myfunction()
print(d)