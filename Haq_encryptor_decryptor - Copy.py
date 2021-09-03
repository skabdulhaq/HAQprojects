alphabits= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(',
            ')', '_', '+', '=', '-', '}', '{', ':', '>', '<', '.', ',', ';','1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0', "'", '"',"|",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','`',"~"," ",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(',
            ')', '_', '+', '=', '-', '}', '{', ':', '>', '<', '.', ',', ';','1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0', "'", '"',"|",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','`',"~"," ",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(',
            ')', '_', '+', '=', '-', '}', '{', ':', '>', '<', '.', ',', ';','1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0', "'", '"',"|",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','`',"~"," ",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(',
            ')', '_', '+', '=', '-', '}', '{', ':', '>', '<', '.', ',', ';','1', '2', '3', '4', '5',
            '6', '7', '8', '9', '0', "'", '"',"|",'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','`',"~"," "]
print(len(alphabits))
end = False
while end == False :
    options = input("To encrypt message type 'encode'\nTo decrypt message type 'decode'\n ").lower()
    txt = input("Type your message\n")
    if options == "encode":
        passnumber = int(input("Please create a passcode of decryption \n[NOTE-: passcode must be in between (1 to 190)] \n"))
    else:
        passnumber = int(input("Please Enter a passcode of decryption\n"))
    exit = input("To Encode or Decode type other message type YES \nTo Exit type NO").upper()
    if exit == "no":
        end == True
def Haq_encryptor_decryptor(en_de,input_text,pass_set):
    final_txt = ""
    pass_set_open = True
    final_print = "En"
    if en_de == "decode":
        final_print = "De"
        pass_set_open = False
    if pass_set_open == False:
        pass_set*-1
    for en_de_int in input_text:
        position = alphabits.index(en_de_int)
        final = alphabits[position+pass_set]
        final_txt +=final
    print(f"Your {final_print}crypted text is down \n{final_txt}")
