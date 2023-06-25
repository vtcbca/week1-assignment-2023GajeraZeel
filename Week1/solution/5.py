# Write a python script to enter any string and count vowel.
v=input("Enter a string:")
count=0
v=v.lower()
for i in v:
    if(v =='a'or v =='e'or v =='i' or v == 'o' or v =='u'):
        count=count+1
    print("vowel:",count)
