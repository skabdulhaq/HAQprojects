#import subprocess

#subprocess.call(["cls"])
print("Hi Welcome To BMI calculator.")
# this is written to check the print statement
# bmi1 = float(input("bmi= "))
weight = float(input("Enter your Weight in Kilograms => "))
height1 = float(input("Enter your Height in Feet => "))
height=height1/3.33
bmi1 = float(weight/height**2)
bmi = round(bmi1, 2)
if bmi <= 18.5:
    print(f"Your BMI Is {bmi},Your Under Weight,Don't Feel Shy To Eat.")
elif 18.5 < bmi <= 25:
    print(f"Your BMI Is {bmi},Your Normal Weight,Keep It Up Your healthy.")
elif 25 < bmi <= 30:
    print(f"Your BMI Is {bmi},Your Over Weight,Exercise Everyday To Become healthy.")
elif 30 < bmi <= 35:
    print(f"Your BMI Is {bmi},Your Have Obesity ,Exercise Everyday To Become healthy & Consult A Doctor.")
else:
    print(f"Your BMI Is {bmi},Your Have Overly Obesity ,Exercise Everyday To Become healthy & Consult A Doctor.")
min_ideal_weight_for_height = round(19*height**2, 2)
max_ideal_weight_for_height = round(25*height**2, 2)
print(f"For Your height weight must be between {min_ideal_weight_for_height} - {max_ideal_weight_for_height} . ")
input("Any thing to exit.")