#You will simulate a task manager.
#The program will generate an X number of tasks (input from the user). Each task will have a title, duration (in mins)
# and a priority (also input from the user), lower value of priority the higher it is.
# Use a single list to hold the tasks in it and to be used as a queue.

#You will implement your own functions for the queue (insert, extract, peek, is_empty).
#Your program will have the following functions (other than the queue related ones):
#`complete_next_task`: will take the queue as argument and will print and extract the highest priority task
#`search_for_task`: will take the queue and title as arguments and search for that set title. (you have to use Binary Search Algorithm)
#`sort_tasks`: will take queue as argument and will return a new queue have tasks sorted duration (ascending or descending your choice)
#make all the needed checks for the inputs and handle exceptions.



# ---------------- Queue Functions ----------------

def insert(queue, task):
    queue.append(task)

def extract(queue):
    if not is_empty(queue):
        return queue.pop(0)
    return None

def peek(queue):
    if not is_empty(queue):
        return queue[0]
    return None

def is_empty(queue):
    return len(queue) == 0


def complete_next_task(queue):
    if is_empty(queue):
        print("\nNo tasks left to complete!")
        return

    # Find task with highest priority (lowest number)
    min_priority = queue[0]['priority']
    index = 0
    for i in range(1, len(queue)):
        if queue[i]['priority'] < min_priority:
            min_priority = queue[i]['priority']
            index = i

    task = queue.pop(index)
    print(f"\nCompleted: {task['title']} (Priority {task['priority']})!")

def sort_tasks(queue):
    # Return a new list sorted by duration ascending
    sorted_queue = queue.copy()
    for i in range(len(sorted_queue)):
        for j in range(i + 1, len(sorted_queue)):
            if sorted_queue[i]['duration'] > sorted_queue[j]['duration']:
                temp = sorted_queue[i]
                sorted_queue[i] = sorted_queue[j]
                sorted_queue[j] = temp
    return sorted_queue

def search_for_task(queue, title):
    # Sort alphabetically before binary search
    sorted_queue = queue.copy()
    for i in range(len(sorted_queue)):
        for j in range(i + 1, len(sorted_queue)):
            if sorted_queue[i]['title'].lower() > sorted_queue[j]['title'].lower():
                temp = sorted_queue[i]
                sorted_queue[i] = sorted_queue[j]
                sorted_queue[j] = temp

    title = title.lower()
    low = 0
    high = len(sorted_queue) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_title = sorted_queue[mid]['title'].lower()
        if mid_title == title:
            task = sorted_queue[mid]
            print(f"🔍 Found: {task['title']} ({task['duration']} mins), priority {task['priority']}")
            return
        elif mid_title < title:
            low = mid + 1
        else:
            high = mid - 1

    print("No matching task found.")


def main():
    tasks = []  # queue list

    print("Welcome to your Task Manager!")
    print("Let's add some tasks.")
    
    # Input number of tasks
    while True:
        try:
            num_tasks = int(input("How many tasks do you want to add? "))
            if num_tasks > 0:
                break
            else:
                print("Please enter a number greater than 0.")
        except:
            print("Oops! Please enter a valid number.")
    
    # Add tasks
    for i in range(num_tasks):
        print(f"\nTask {i+1}:")
        title = input("What's the task name? ").strip()
        
        while True:
            try:
                duration = int(input("How many minutes will it take? "))
                if duration > 0:
                    break
                else:
                    print("Duration must be more than 0 minutes.")
            except:
                print("Please enter a number for minutes.")
        
        while True:
            try:
                priority = int(input("Priority (1=highest, 2=next, etc.): "))
                if priority > 0:
                    break
                else:
                    print("Priority must be greater than 0.")
            except:
                print("Please enter a positive number for priority.")
        
        task = {
            'title': title,
            'duration': duration,
            'priority': priority
        }
        insert(tasks, task)
        print(f"Added: {title}")
    
    # Menu
    while True:
        print("\nWhat would you like to do?")
        print("1. See all tasks")
        print("2. Complete next task")
        print("3. Find a task")
        print("4. Sort tasks by duration")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            if is_empty(tasks):
                print("\nNo tasks!")
            else:
                print("\nAll Tasks:")
                for task in tasks:
                    print(f"- {task['title']} ({task['duration']} mins), priority {task['priority']}")
        
        elif choice == "2":
            complete_next_task(tasks)
        
        elif choice == "3":
            title = input("Enter task name to search: ").strip()
            if title:
                search_for_task(tasks, title)
            else:
                print("Task name can't be empty.")
        
        elif choice == "4":
            sorted_list = sort_tasks(tasks)
            print("\nTasks Sorted by Duration:")
            for task in sorted_list:
                print(f"- {task['title']} ({task['duration']} mins), priority {task['priority']}")
        
        elif choice == "5":
            print("\n👋 Goodbye!")
            break
        
        else:
            print("Please enter a number between 1 and 5.")


main()
