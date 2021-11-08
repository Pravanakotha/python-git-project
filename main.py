num = int(input("Enter number to check:"))
sum = 0
temp = num
while num>0:
    rem = num%10
    sum = sum * 10 +rem
    num = num // 10
if temp==sum:
    print("Palindrome")
else:
    print("Not a palindrome")