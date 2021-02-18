#todo_list.py
#the program allows user to add and display a list of tasks to complete
#Sam Hurd, 15 Feb 21


#list
todo_list  = ['\n\nBuy food', 'Do homework', 'Make dinner']


#main routine
def my_list():
    i = 1
    while i < 2:

        try:

            options = int(input("\nChoose a mode by entering a number:\n1. Add a task\n2. View list\n3. Exit\n\n"))
            if options == 1:
                user_todo = input("What is something you want to add to your to-do list:")
                todo_list.append(user_todo)
                print("Your task has been added.")
            elif options == 2:
                print('\n\n'.join(todo_list))
                print('\n\nYour task has been printed.')
            elif options == 3:
                print('\n\nGoodbye!')
                i += 3
            else:
                print("\n\nThat is not a valid choice. Please enter a number from 1 to 3.")
            
        
        except ValueError:
            print("That is not an option, please enter a number")
    return options
            



my_list()