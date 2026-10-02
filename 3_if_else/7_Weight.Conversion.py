# Weight conversion Program
x,y=0,0
con=input('Press p - for kg to pounds \n' \
      'Press k- for pounds to kg: ').lower()

if con=='p':
    x=float(input('Enter the weight in Kg: '))
    var1=x*2.20
    print(f'Weight in Pounds is {x}lbs.')
elif con=="k":
    y=float(input('Enter the weight in Pounds: '))
    var2=y/2.20
    print(f'Weight in Kilograms is {y}kg.')

else:
    print('You Entered Wrong Character.')