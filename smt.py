#hello yall, i luv u
#if the code doesnt work try to add the other problems into a comment 
#no cap, I appreciate you always explaining things clearly. You guys are GOATS.
#problem1
num = int(input("Enter the Fibonacci number : "))

if num < 0:
  print("number must be non-negative")
else:
  a, b = 0, 1
  for i in range(num):  
    a, b = b, a + b

  print(f"The {num}th Fibonacci number is: {a}")

#problem2
tasks = []


def addTask():
  title = input("Enter task title: ")
  tasks.append({"title": title, "completed": False})
  print(f"Task '{title}' added!")


def viewTasks():
  if not tasks:
    print("There are no tasks on your list.")
  else:
    print("Tasks:")
    counter = 1
    for task in tasks:
      completion = "completed" if task["completed"] else ["pnding"]
      print(f"{counter} {task['title']} ({completion})")
      counter = counter+1
def markTaskCompleted():
  taskNumber = int(input("Enter task number to mark complete: ")) - 1
  if 0 <= taskNumber < len(tasks):
    tasks[taskNumber]["completed"] = True
    print(f"Task '{tasks[taskNumber]['title']}' marked complete!")
  else:
    print("Invalid task number. Please try again.")
def deleteTask():
  taskNumber = int(input("Enter task number to delete: ")) - 1
  if 0 <= taskNumber < len(tasks):
    for i in range(taskNumber, len(tasks) - 1):
      tasks[i] = tasks[i + 1]
    tasks = tasks[: len(tasks) - 1]
    print(f"Task deleted successfully!")
  else:
    print("Invalid task number. Please try again.")
while True:
  print("To-Do List Menu:")
  print("1. Add Task")
  print("2. View Tasks")
  print("3. Mark Task Completed")
  print("4. Delete Task")
  print("5. Exit")
  choice = input("Enter your choice (1-5): ")
  if choice == "1":
    addTask()
  elif choice == "2":
    viewTasks()
  elif choice == "3":
    markTaskCompleted()
  elif choice == "4":
    deleteTask()
  elif choice == "5":
    print("fe dhya ")
    break
  else:
    print("Invalid choice. Please try again.")

    
#problem3 :got some backup from a friend
users = {}

def registeruser(username):
  if username in users:
    print(f"Username '{username}' already exists. Please choose a different one.")
    return

  users[username] = {"username": username, "chat_history": []}
  print(f"Welcome, {username}! You are now registered.")

def sendmessage(sender, recipient, message):
  if recipient not in users:
    print(f"User '{recipient}' not found.")
    return

  users[sender]["chat history"].append(f"Sent to {recipient}: {message}")
  users[recipient]["chat history"].append(f"From {sender}: {message}")
  print(f"Message sent from {sender} to {recipient}.")

def viewmessages(username):
  if not users[username]["chat history"]:
    print(f"{username}, you have no messages in your history.")
    return

  print(f"Chat History for {username}:")
  for message in users[username]["chat history"]:
    print(message)

while True:
  action = input("Enter action (register, send, view, quit): ")
  if action == "register":
    username = input("Enter username: ")
    if username not in users: 
      registeruser(username)
  elif action == "send":
    sender = input("Enter your username: ")
    if sender in users:
      recipient = input("Enter recipient username: ")
      message = input("Enter message: ")
      sendmessage(sender, recipient, message)
  elif action == "view":
    username = input("Enter username to view history: ")
    if username in users:
      viewmessages(username)
  elif action == "quit":
    print("Exiting chat system.")
    break
  else:
    print(f"Invalid action. Please try again.")

