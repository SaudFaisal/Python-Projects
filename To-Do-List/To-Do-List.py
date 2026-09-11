#create get_number to avoid ValueError
#create an empty list











def get_number(text):
     try:
          a = int(input(text))
          return a
     except ValueError:
          print("That's not a number,Try again")
          return None
        



task = []

while True:
    choice = get_number("Select which option you want:\n1 - Add task\n2 - Delete task\n3 - Show tasks\n4 - Quit\nType the number here: ")
    if choice is None:
         continue
    if choice == 1:
        task.append(input("Enter the task: "))
        continue
    elif choice == 2:
        if len(task) == 0:
                print("There is no tasks.")
                continue
        for Index, Tasks in enumerate(task):
            print(f"Index: {Index} ,Tasks: {Tasks}")
        deltask = get_number("Enter the number of the Index you want to delete: ")
        if  deltask is None:
             continue
        if len(task) > deltask:
             del task[deltask]
        else:
            print("There is no task with that Index.")
        continue
    elif choice == 3:
        if len(task) == 0:

                    print("There is no tasks.")
        for Index, Tasks in enumerate(task):
            print(f"Index: {Index}, Tasks: {Tasks}")
        continue
    elif choice ==4:
        print("GoodBye!")
        break
    else:
        print("That's not an option,Try again.")
        continue
       


