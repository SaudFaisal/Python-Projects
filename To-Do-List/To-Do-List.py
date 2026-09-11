'''
1.create get_number to avoid ValueError
2.create an empty list[]
3.create a loop while True so that code keep playing until the user wants to quit
4.choice = input 1,2,3,4
5.1 = add task , 2 = delete task , 3 = show tasks , 4 = Quit
6.add task use task.append(input()) so that the user enter a task and the task stores it in the list[]
7.delete task user len(task)=0 to know if there is any task stored if no then continue from the beginning
8.use for with 2 variable and enumerate(task): so that is shows what is inside the list with the Index of it 
9.deltask = the number of Index wanted to delete , use len(task) > deltask so that if the user type an Index not in the list it prevent this from happening
10.del task[deltask] this delete the task in the list remember deltast = Index 
11.show tasks we use if len(task) == 0 if no task print no task , we use for and enumerate(task) to print the Index and the task in the list
12.Quit we print GoodBye! and break the loop
'''

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
       


