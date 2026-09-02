#Start
# input number
# if numb == 0 
# numb = 0 
# if numb postive or negative
# if % == 0 
# Even number
# else 
# Odd number 
#End




numb = int(input("Enter a number: "))



if numb == 0 :
    print("Your number is Zero")
elif numb > 0:
    print("Your number is positive")
else:
    print("Your number is Negative")

if numb ==0:
    print("")
elif numb % 2 == 0 :
    print(f"The number {numb} is even")
else:
    print(f"The number {numb} is odd")