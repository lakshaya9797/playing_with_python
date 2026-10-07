import time

x=int(input("Enter time in seconds: "))
for i in range(x,0,-1):
    sec=i%60
    min=int(i/60)
    hr=int(i/3600)
    time.sleep(1)
    print(f"{hr}:{min}:{sec}")
print("Time's Up")