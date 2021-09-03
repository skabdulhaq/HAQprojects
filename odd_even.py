import subprocess

subprocess.call("clear", shell="true")
number= (input("Type The Number To Know It Is Even Or Odd => "))
operation= (number)%2
if operation == 0 :
    print("Your Number Is Even.")
else :
    print ("Your Number Is Odd. ")



