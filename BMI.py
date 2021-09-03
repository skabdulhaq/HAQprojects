import subprocess

subprocess.call("cls" ,shell="true")
print("Hi Welcome To BMI calculator.")
weight=(input("Enter your Weight in Kilograms => "))
height=(input("Enter your Height in Meters => "))
BMI=float(weight)/float(height)** 2
result=round(BMI)
print(f"Your BMI is = {result}")


#print(type(height))