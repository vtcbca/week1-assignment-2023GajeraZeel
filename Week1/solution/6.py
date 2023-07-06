# Write a python script to enter any string and print only part of string. Take input of start character and end character from user.
oldString = input("enter a string:")
count = 0
for i in oldString:
      count = count + 1
newString = oldString[ 0:2 ] + oldString [count - 2: count ]
print("Input string = " + oldString)
print("New String = "+ newString)
