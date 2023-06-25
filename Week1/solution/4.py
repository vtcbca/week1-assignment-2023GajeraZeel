#to check whether number is armstrong number or not
num=int(input("Enter a number to be checked:"))
result=0
a=num
for i in range(num):
     if num!=0:
         r=num%10
         result+=r*r*r
         num//=10
if result==a:
     print("is a armstrong number")
else:
    print("is not a armstrong number")
