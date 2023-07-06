# Write a python script to enter any string, replace vowel with its position number.
a=input("Enter string :")
n=""
for i in range(len(a)):
    if i%2!=0:
        n+=a[i]
    else:
        n+=str(i)
print(n)
