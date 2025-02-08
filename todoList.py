def View_Tasks(tasks):
    if len(tasks) == 0:
        print("No tasks in the list")
    else:
        for task in enumerate(tasks,1):
            print(f'{task[0]}.{task[1]}')

def add_Task(tasks):
    while True:
      task_to_append = input("Enter a new task: ").strip()
      if len(task_to_append) == 0:
          print("Invalid task!")
      else:
          tasks.append(task_to_append)
          break

def removeTask(tasks):
    View_Tasks(tasks)
    while True:
        try:
            indexOfTask = int(input("Enter the task number: "))
            if(1<=indexOfTask<=len(tasks)):
                tasks.pop(indexOfTask-1)
                break
            else:
                print("Invalid Task Number")
        except Exception as e:
            print("Invalid task number")
    

def main():
    tasks = []
    while True:
        try:
            print()
            print("Todo List Menu")
            print("1. View Tasks")
            print("2. Add a Task")
            print("3. Remove a Task")
            print("4. Exit")

            userChoice = int(input("Enter your choice: "))
            if userChoice == 1:
                View_Tasks(tasks)
            elif userChoice == 2:
                add_Task(tasks)
            elif userChoice == 3:
                removeTask(tasks)
            elif userChoice == 4:
                print("Exiting the program...")
                break
            else:
                print("Invalid choice")
        except Exception as e:
            print("Invalid choice")
            
if __name__ == "__main__":
    main()