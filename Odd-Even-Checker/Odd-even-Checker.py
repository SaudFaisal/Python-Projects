#import arabic and shape it to use it later in the code

import arabic_reshaper
from bidi.algorithm import get_display

def ar(text):
    lines = text.split("\n")
    result= []
    for line in lines:
        reshaped = arabic_reshaper.reshape(line)
        result.append(get_display(reshaped, base_dir='L'))
    return '\n'.join(result)


#input choice , numb
#make 2 def (is_even) and (get_number) the first for checking if its even the second for the ValueError so that the user cannot enter a wrong Value.
#While true so that the function keep working until user decide to exit
#use try function so that when ever the user type a word instead of a number will not show error instead will do the loop again with printing("That's not a number, Try again.") that is the def get_number function is .
#choice =  let user choose a number from 1 - 3. (made a def function (ar) and (get_number) )
#if choice = 1 then odd-even checker will start (add the get_number functon ) (used the is_even function)
#if choice = 2 then positive negative checker will start (add the get_number function)
#if choice = 3 then the program will break(exit)
#any number not from the list will print("invalid choice, Try again.")
#we use if to submit the input to the function 
# Example .. if user choose 1 we say [if choice ==1: then do odd checker and like that to the rest]


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def get_number(prompt):
    try:
        numb = int(input(prompt))
        return numb
    except ValueError:
        print("That's not a number, Try again.")
        return None


while True:
        choice = get_number(ar("1 - فحص زوجي/فردي\n2 - فحص موجب/سالب\n3 - الخروج\nChoice from the list: "))
        if choice is None:
            continue
        if choice == 1:
            numb = get_number("Enter the number:")
            if numb is None:
                continue
            if numb == 0:
                print(f"The number {numb} is zero.")
            else:
                x = is_even(numb)
                if x:
                    print(f"The number {numb} is even.")
                else:
                    print(f"The number {numb} is odd.")

        elif choice == 2:
            numb = get_number("Enter the number: ")
            if numb is None:
                continue        
            if numb == 0:
                print(f"Your nummber is zero")
            elif numb > 0 :
                print(f"Your number {numb} is positive")
            else:
                print(f"Your number {numb} is negative")

        elif choice == 3:
            print("GoodBye!")
            break

        else:
            print("invalid choice, Try again.")