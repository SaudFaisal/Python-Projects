#First def the get_number() -> use for if the user put a wrong value instead of a number will not crash the code


def get_number(b):
    try:
        a = int(input(b))
        return a
    except ValueError:
        print("That's not a number,Try again.")
        return None

#start with while so that the get_number() function work [don't forget the if var is None: continue] so that when the user enters wrong value code restart from the beginning 
#input: start , end ,jumps
#jump != 0 add if user enters 0 let jump = 1
#use for range function 
#use if to sperate to for functions one if end > start should print normally second if that start was bigger should reverse the for function by letting jump = (-jump)
#use end + 1 or end - 1 so u get the right value
#output should be a series of number
#break



while True:

    start = get_number("Enter a number to start from: ")
    if start is None:
        continue

    end = get_number("Enter a number to end at: ")
    if end is None:
        continue

    jump = get_number("Enter the step size: ")
    if jump == 0:
        jump = 1
    if jump is None:
        continue

    if end > start :
        for i in range(start, end + 1, jump):
            print(i)
    else:
        for i in range(start, end - 1, -jump):
            print(i)
    break