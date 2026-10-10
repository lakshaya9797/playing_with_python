p=float(input("Enter Principle: "))
while p<=100000:
    print(f"Principal can't be smaller than {p}")
    p=float(input("Enter Principal again: "))

r=float(input("Enter rate: "))
while r<=0:
    print(f"rate can't be smaller than {r}")
    r=float(input("Enter rate again: "))

t=float(input("Enter time period: "))
while t<=0:
    print(f"Time period can't be smaller than {t}")
    t=float(input("Enter Time period again: "))

n=float(input("Enter Number of compounding periods: "))
while n<=0:
    print(f"Compounding period can't be smaller than {n}")
    n=float(input("Enter Compounding period again: "))

a=p*pow(1+r/100*n,n*t)
ci=a-p
print(f"Your Compound Interest is {ci:.2f}")