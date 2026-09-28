# Foramt specifier formats a value based on the flags given to it.

p=9.8833
q=-8.2423
r=98234.989

print(f'{p:.2f}')
print(f'{q:.3f}')
print(f'{r:.4f}')   # "." is used to tell the interpreter that it have to print n(eg. 2,3) numbers after the .(decimatl)  

print(f"{p:10}")        # this will allocate 10 spaces to variable p

print(f'{q:,}')         # this will seperate the Thousands place by ","

print(f'{r:<12,}')       # right justify 12 spaces
print(f'{r:>12,}')       # left justify 12 spaces
print(f'{r:^12,}')       # center justify with 12 spaces


