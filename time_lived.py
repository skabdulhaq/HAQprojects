#import subprocess

#subprocess.call("cls" , shell="true")
print("Do You Know How Much Time You Have Lived ?\nLets Check")
age =input("Please Enter Your Age => ")
cal_seconds = int(age)*365*24*60*60
cal_minutes = int(age)*365*24*60
cal_hours = int(age)*365*24
cal_days =int(age)*365
cal_weeks =int(age)*52
cal_months =int(age)*12
print(f"Ho You Enjoyed {cal_seconds} seconds or {cal_minutes} Minutes or {cal_hours} hours or {cal_days} Days or {cal_weeks} weeks or {cal_months} months.")

input("Type any thing to stop")

