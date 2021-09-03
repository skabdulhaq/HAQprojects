import random
print("Welcome to B_UN_Hackable password generator")
# letters = input("le").split( )
# print(letters)
letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols_list = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '-`', '}', '{', ':', '>', '<', '.', ',', ';']
numbers_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
user_let = int(input("How many letters should be there in password that your generating => "))
user_spc = int(input("How many special characters should be there password in that your generating => "))
user_num = int(input("How many numbers should be there in password that your generating => "))
password_list = []
#'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for letters in range(1, user_let+1):
    letter = random.choice(letters_list)
    password_list.append(letter)
# print(password_list)
for symbols in range(1, user_spc+1):
    sym = random.choice(symbols_list)
    password_list.append(sym)
# print(password_list)
for numbers in range(1, user_num+1):
    num = random.choice(numbers_list)
    password_list.append(num)
# print(password_list)
random.shuffle(password_list)
# print(password_list)
password = ""
for x in password_list:
    password = password+x
print(f"Your Un Hackable password is => {password}" )
input("Press Enter To EXIT.")