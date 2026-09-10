
'''
1.create get_number for Value error and setup quit option as str first then make it int
2.use while true so it be on a loop until the user wants to quit
3.input num1 , num2 , oper
4.let user chose from 1-4
4. 1 = add , 2 = subtract , 3 = multiply , 4 = divide
5.make sure to use if for None for the get_number and if =="quit" so he can quit the code
6.use if statement to check whether the user choose from if = 1 the do add and so one using elif
7.make sure no logical error like divide by zero fix it by if statement
'''




def get_number(text):
    try:
        exitcode = input(text)
        if exitcode == "q" or exitcode == "quit":
            print("Goodbye!")
            return "quit"
        else:
            a = int(exitcode)
            return a 
    except ValueError:
        print("That's not a number,Try again.")
        return None 
            


while True:
    num1 = get_number("Enter the First number To quit type q or quit: ")
    if num1 is None:
        continue
    if num1 == "quit":
        break
    oper = get_number("Enter which operator \n1 - Addition\n2 - Subtraction\n3 - multiplication\n4 - division\nTo quit type q or quit \nEnter your opition here: ")
    if oper is None:
        continue
    if oper == "quit":
            break
    num2 = get_number("Enter the Second number To quit type q or quit: ")
    if num2 is None:
        continue
    if num2 == "quit":
            break

    if oper == 1:
        print(num1 + num2)
    elif oper == 2:
        print(num1 - num2)
    elif oper == 3:
        print(num1 * num2)
    elif oper == 4:
        if num2 == 0:
            print("You cannot divide by Zero")
        else:
            print(num1 / num2)
    else:
        print("Thats not an opition,Try again.")
        continue
    


