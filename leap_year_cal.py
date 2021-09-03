#import subprocess

#subprocess.call(["clear"])
print("Welcome To Leap Year Calculator.")
year = input("Please Enter Year => ")
# year = input("year=> ")
a = year % 4
b = year % 100
c = year % 400
if a==0 :
    if b==0:
        if c==0:
            print("this is a leap year.")
        else:
            print("this is not a leap year.")
    else:
        print("this is a leap year.")
else:
    print("this is not a leap year.")

input("Type any thing to stop.")

