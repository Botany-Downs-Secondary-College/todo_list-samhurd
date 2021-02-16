todo_list  = ['\n\nBuy food', 'Do homework', 'Make dinner']


def my_list():
    i = 1
    while i < 2:

        try:

            options = int(input("\nChoose a mode by entering a number:\n1. Add a task\n2. View list\n3. Exit\n\n"))
            if options == 1:
                user_todo = input("What is something you want to add to your to-do list:")
                todo_list.append(user_todo)
                print("Your task has been added.")











my_list()