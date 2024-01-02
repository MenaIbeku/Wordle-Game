# Author   : Mena Ibeku
# Email    : cibeku@umass.edu
# Spire ID : 34151261
def get_guess():
    user_input = input("What word is this?:")
    if len(user_input) >5:
        user_input = (user_input[0:5])
    return user_input.upper()

def print_word(string):
    empty_list=""
    for i in string:
        empty_list += i + " "
    print(empty_list.rstrip())


        
    

def exact_match_compare(string1,string2):
    full_string = ""
    i=0
    j=0
    while i<=len(string1)-1 and j<=len(string2)-1:
        if string1[i] == string2[j]:
            full_string+="🟢"
        else:
                full_string+="🔴"
        i+=1
        j+=1
    return full_string


def one_turn(solution):
     mena=get_guess()
     print_word(mena)
     lerned= exact_match_compare(solution,mena)
     print(lerned)
     if lerned == "🟢🟢🟢🟢🟢":
          print("Congratulations")
          exit()
                
def make_solution():
     import random
     word_bank = ["WHICH", "THEIR","THERE", "WOULD", "OTHER", "THESE", "ABOUT", "FIRST", "COULD", "AFTER"]
     return random.choice(word_bank)



