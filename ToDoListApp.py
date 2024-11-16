

print("Welcome to the To-Do List App!")

def menu_options():

    print("Menu Options: \n"\
            "1. Add a Task\n"\
            "2. View Tasks\n"\
            "3. Mark a task as complete\n"\
            "4. Remove a task\n"\
            "5. Quit\n")


def add_task(tasks):
    task = input("Please enter a task description: ")
    tasks.append(task)
    print("Task has been added successfully!")


def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks in list.")
    else:
        print('Tasks:\n')
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def mark_complete(tasks):
    if len(tasks) == 0:
        print("No tasks to mark as complete.")
        return
    
    try:
        marked_task = int(input("Enter the task number to mark as complete: ")) 

        if 1 <= marked_task <= len(tasks):
            tasks[marked_task - 1] 
            print(f"Task {marked_task} is now complete.")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def remove_task(tasks):
    if len(tasks) == 0:
       print("No tasks to delete. ")
       return
    
    try:
        task_number = int(input("Enter task number to be removed. "))
        
        if 1 <= task_number <= len(tasks):
            remove_task = tasks.pop(task_number - 1)
            print(f"Task {remove_task} has been removed. ")
        else:
            print("Invalid task number.") #this prints no matter what task I choose to remove

    except AttributeError:
            print("Please enter a valid task number.")
    except ValueError:
            print("Nothing has been removed. ")


def main():
    tasks = []
    while True:
        menu_options()        

        try:

            option = input("Please pick an option: ")

            if option == '1':
                add_task(tasks)
            elif option == '2':
                view_tasks(tasks)
            elif option == '3':
                mark_complete(tasks)
            elif option == '4':
                remove_task(tasks) 
            elif option == '5':
                print("Thank you for using our To-Do List Application. Until Next time!")
                break
            else:
               print("Invalid option: Please pick a option number between 1 and 5") 

        except ValueError:
            print("Please enter a valid number")
      
if __name__ == "__main__":
    main()