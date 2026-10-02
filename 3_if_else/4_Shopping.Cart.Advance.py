# Shopping Cart Program
order1, order2, order3='a','b', 'c'
t=0
p1,p2,p3=60,50,10
quant1, quant2, quant3=0,0,0
r1, r2, r3= 'a', 'b', 'a'
print('\nThese are the items you can buy.\n'
                        '1. Banana- Rs60\n'
                        '2. Apple - Rs50\n' 
                        '3. Pen - Rs10')
print('Note: type the exact spelling of the item which is mentioned above.')
r1=input('Press Y if you want to order something otherwise press N.').lower()
if r1=='y':
    order1=input("Enter the First item : ").lower()
    quant1=int(input('Enter the Quantity of the item : '))
    if order1=='banana':
        t+=p1*quant1
    elif order1=='apple':
        t+=p2*quant1
    elif order1=='pen':
        t+=p3*quant1
    r2=input('\nPress Y if you want to order more otherwise press N: ').lower()
    
    if r2=='y':
        order2=input('Enter the Next item : ').lower()
        quant2=int(input('Enter the Quantity of the item : '))
        if order2=='banana':
            t+=p1*quant2
        elif order2=='pen':
            t+=p3*quant2
        elif order2=='apple':
            t+=p2*quant2
        r3=input('\nPress Y if you want to order more otherwise press N: ').lower()
        
        if r3=='y':
            order3=input('Enter the Next item : ').lower()
            quant3=int(input('Enter the Quantity of the item : '))
            if order3=='banana':
                t+=p1*quant3
            elif order3=='apple':
                t+=p2*quant3
            elif order3=='pen':
                t+=p3*quant3
            print(' HERE IS YOUR Bill')
            print(f' Your Total :{t}')
            print('Thanks for visiting us.')    
                
        elif r3=='n':
            print(' HERE IS YOUR Bill')
            print(f' Your Total :{t}')
            print('Thanks for visiting here. ')

    elif r2=='n':
        print(' HERE IS YOUR Bill')
        print(f' Your Total :{t}')
        print('Thanks for visiting us.')

elif r1=='n':
    print('Thanks for visiting here ')

