# to enter any number and print the sum of its digit.
num=int(input("enter 3 digiti a number:"))
sum=0
while(num!=0):
    sum=sum+(num%10)
    num=num//10
print("sum is:",sum)
