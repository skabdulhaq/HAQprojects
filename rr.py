final_txt = "hi"
final_print = "en"
confer = input("Do you want to save the file on desktop or just read hear\nTo read hear type 'yes'\nTo save it on Desktop just press Enter\n=>>  ").lower()
if confer == "yes":
    print(f"your {final_print}crypted text\n{final_txt}")    
else:
    import pathlib, os
    desktop = pathlib.Path.home() / 'Desktop'
    os.chdir(desktop)
    txt_name = input("Do u want to name your file\nIf yes then type 'yes'\nOr press Enter to generate a random name\n=>> ").lower()
    if txt_name == "yes`":
        name_1 = input("Enter name your file =>")
        name = name_1+".txt"
        with open(name, "w") as text :
            text.write(final_txt)
        print(f"your {final_print}crypted text is in the desktop named '{name}' ")
    else:
        import random
        suff = random.randint(0,123456)
        name = f"{final_print}crypted_{suff}.txt"
        with open(name, "w") as text :
            text.write(final_txt)
        print(f"your {final_print}crypted text is in the desktop named '{name}' ")
