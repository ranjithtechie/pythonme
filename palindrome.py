num = int (input ("Enter a number "))
store=num
ref=0
while (num>0):
    ans=num%10
    ref=ref*10+ans
    num=num//10
if ref==store:
        print("The number is palindrome ")
else :
        print ("Not a palindrome")
