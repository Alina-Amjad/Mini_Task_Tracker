import json

filename="tasks.json"

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except:
        return [] # If Json file doesn't Exist will return [] for the program to continue

def save_tasks(data):
    with open("tasks.json","w") as f:
        json.dump(data,f) # saving data into json file

def add_task():
    task_title=input("Enter Task Title: ")
    if not task_title: # Checking for title to be not empty
        print("Error: Task Title can't be empty")
        return
    tasks.append({"title":task_title,"done":False})
    print("Task Added")
    save_tasks(tasks)

def view_tasks():
    if not tasks:
        print("No Tasks Available")
    for i,tsk in enumerate(tasks,1):
        status="Done" if tsk["done"] else "Pending" # Calling undone tasks as Pending and if if tsk["done"] is True it shows Done else Pending.
        print(f"{i}. {tsk['title']} [{status}]")

def complete_task():
    if not tasks: # in case no task exists
        print("No Task to complete")
        return
    view_tasks()
    try:
        task_complete=int(input("Enter Task number to Complete: "))
        if 1<=task_complete<=len(tasks): # making sure that the task choice is within the limit
            tasks[task_complete-1]["done"]=True
            save_tasks(tasks)
            print("Task Completed")
        else:
            print("Invalid Task Number")
    except:
        print("Invalid Task Number")

def delete_task():
    if not tasks: # in case no task exists
        print("No Task to delete")
        return
    view_tasks()
    try:
        task_delete = int(input("Enter Task number to Delete: "))
        if 1<=task_delete<=len(tasks):   # making sure that the task choice is within the limit
            deleted=tasks.pop(task_delete-1)
            save_tasks(tasks)
            print(f"Task {deleted['title']} Deleted")
        else:
            print("Invalid Task Number")
    except:
        print("Invalid Task Number")

tasks=load_tasks() #
while True:
    print("-"*7+"Task Tracker"+"-"*7)
    print("\n1. ADD     2. View     3. Complete     4. Delete       5. Exit\n")
    try:
        choice=int(input("Enter your choice: ").strip()) # To keep the choice between 1 and 5
    except:
        print("Invalid Choice. Please Choose between 1 and 5")
        continue
    if choice==1:
        add_task()
    elif choice==2:
        view_tasks()
    elif choice==3:
        complete_task()
    elif choice==4:
        delete_task()
    elif choice==5:
        print("Exiting...")
        break
    else:
        print("Invalid Choice. Please Choose between 1 and 5")