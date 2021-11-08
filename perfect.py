import math
n = int(input("Enter number to check:"))
res = math.sqrt(n)
if(int(res)==math.sqrt(n)):
    print("Perfect Square")
else:
    print("Not a perfect square")