#  to check palindrom number
num=int(input("enter a number :"))
reverse=0
a=num
while(num!=0):
    remainder=num%10
    reverse=reverse*10+remainder
    num//=10
if a==reverse:
    print("is a palindrome number")
else:
    print("is not a palindrome number")
