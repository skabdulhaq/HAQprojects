#import subprocess

#subprocess.call("cls" , shell="true")
print("Do You Know How Much Time You Are Going To Live ?\nLets Check")
age =input("Please Enter Your Age => ")
age_r= 90-int(age)
cal_seconds = int(age_r)*365*24*60*60
cal_minutes = int(age_r)*365*24*60
cal_hours = int(age_r)*365*24
cal_days =int(age_r)*365
cal_weeks =int(age_r)*52
cal_months =int(age_r)*12
print(f"Ho You Are Left With {cal_seconds} seconds or {cal_minutes} Minutes or {cal_hours} hours or {cal_days} Days or {cal_weeks} weeks or {cal_months} months.")
print(f"You Have Only {cal_months} Months Remaining\nSo Dont Waste Your Time.")
input("Type any thing to stop")