# Shopping Cart Program
order='a'
total=0
print('These are the products you can buy.\n'
                        '1. Banana- Rs60\n'
                        '2. Apple - Rs50\n' 
                        '3. Pens - Rs10\n'
                        '4. Computer - Rs1000\n' 
                        '5. Books - Rs200')

order=input("Enter the Product You want to buy.")
order=input("Enter the Product You want to buy.")
order=order.lower()

if order=='banana':
    quant=int((input)(f'how many of {order} you want to buy?'))
    p1=60
    total=p1*quant
if order=='apple':
    quant=int((input)(f'how many of {order} you want to buy?'))
    p2=50
    total=p2*quant
if order=='pens':
    quant=int((input)(f'how many of {order} you want to buy?'))
    p3=10
    total=p3*quant
if order=='computer':
    quant=int((input)(f'how many of {order} you want to buy?'))
    p4=1000
    total=p4*quant
if order=='books':
    quant=int((input)(f'how many of {order} you want to buy?'))
    p5=200
    total=p5*quant

print(' Bill ')
print(f'Your ordered items is {order}\n'
      f'Total Amount to be paid :{total}\n'
      'Thanks for Visiting our Store.')