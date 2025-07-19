#making of a simple calculator
# def calculator():
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))

#     print("choose an operation:" )
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")

#     choice = int(input("enter your choice(1/2/3/4):"))

#     if choice == 1:
#         result = num1 + num2
#         print(f"{num1} + {num2} = {result}")
#     elif choice ==2:
#         result = num1 - num2
#         print(f"{num1} - {num2} = {result}")
#     elif choice == 3:
#         result = num1*num2
    #     print(f"{num1} * {num2} = {result}")
    # elif choice ==4:
    #     if num2 !=0:
    #         result = num1/num2
    #         print(f"{num1} / {num2} = {result}")
         # else:
             # print("error: Division by zero is not allowed.")
    # else :
        # print("error: Invalid choice. ")
# calculator()



### code for TO-DO LIST

#import json
#import os

# DATA_FILE = 'tasks.json'
# 
# Load tasks from JSON file
# def load_tasks():
    # if not os.path.exists(DATA_FILE):
        # return []
    # with open(DATA_FILE, 'r') as file:
        # return json.load(file)

# Save tasks to JSON file
# def save_tasks(tasks):
    # with open(DATA_FILE, 'w') as file:
        # json.dump(tasks, file, indent=4)

# Display all tasks
# def list_tasks(tasks):
    # if not tasks:
        # print("No tasks found.")
    # else:
        # for i, task in enumerate(tasks, 1):
            # status = "✅" if task['completed'] else "❌"
            # print(f"{i}. [{status}] {task['title']} - {task['description']}")

# Add a new task
# def add_task(tasks):
    # title = input("Enter task title: ").strip()
    # description = input("Enter task description: ").strip()
    # task = {'title': title, 'description': description, 'completed': False}
    # tasks.append(task)
    # save_tasks(tasks)
    # print("Task added successfully!")

# Mark a task as completed
# def mark_completed(tasks):
    # list_tasks(tasks)
    # try:
        # task_num = int(input("Enter task number to mark as completed: "))
        # if 0 < task_num <= len(tasks):
            # tasks[task_num - 1]['completed'] = True
            # save_tasks(tasks)
            # print("Task marked as completed.")
        # else:
            # print("Invalid task number.")
    # except ValueError:
        # print("Please enter a valid number.")
# 
# Update a task
# def update_task(tasks):
    # list_tasks(tasks)
    # try:
        # task_num = int(input("Enter task number to update: "))
        # if 0 < task_num <= len(tasks):
            # title = input("Enter new title: ").strip()
            # description = input("Enter new description: ").strip()
            # tasks[task_num - 1]['title'] = title
            # tasks[task_num - 1]['description'] = description
            # save_tasks(tasks)
            # print("Task updated successfully.")
        # else:
            # print("Invalid task number.")
    # except ValueError:
        # print("Please enter a valid number.")

# Delete a task
# def delete_task(tasks):
    # list_tasks(tasks)
    # try:
        # task_num = int(input("Enter task number to delete: "))
        # if 0 < task_num <= len(tasks):
            # removed_task = tasks.pop(task_num - 1)
            # save_tasks(tasks)
            # print(f"Deleted task: {removed_task['title']}")
        # else:
            # print("Invalid task number.")
    # except ValueError:
        # print("Please enter a valid number.")

# Main menu loop
# def main():
    # tasks = load_tasks()

    # while True:
        # print("\n📋 TO-DO LIST MENU")
        # print("1. List all tasks")
        # print("2. Add a new task")
        # print("3. Mark task as completed")
        # print("4. Update a task")
        # print("5. Delete a task")
        # print("6. Exit")
# 
        # choice = input("Choose an option (1-6): ")
# 
        # if choice == '1':
            # list_tasks(tasks)
        # elif choice == '2':
            # add_task(tasks)
        # elif choice == '3':
            # mark_completed(tasks)
        # elif choice == '4':
            # update_task(tasks)
        # elif choice == '5':
            # delete_task(tasks)
        # elif choice == '6':
            # print("Goodbye!")
            # break
        # else:
            # print("Invalid choice. Please choose from 1 to 6.")

# if __name__ == "__main__":
    # main()



#code for contact book

import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r") as file:
        return json.load(file)

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"\nContact '{name}' added successfully!\n")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("\nNo contacts found.\n")
        return
    print("\n--- Contact List ---")
    for idx, contact in enumerate(contacts, 1):
        print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    print()

def search_contact():
    keyword = input("Enter name or phone/email to search: ").strip().lower()
    contacts = load_contacts()
    results = [c for c in contacts if keyword in c['name'].lower() or keyword in c['phone'] or keyword in c['email']]
    
    if results:
        print("\n--- Search Results ---")
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        print()
    else:
        print("\nNo matching contact found.\n")

def update_contact():
    name_to_update = input("Enter the name of the contact to update: ").strip()
    contacts = load_contacts()
    for contact in contacts:
        if contact['name'].lower() == name_to_update.lower():
            print("Leave blank to keep existing value.")
            new_name = input(f"New name [{contact['name']}]: ") or contact['name']
            new_phone = input(f"New phone [{contact['phone']}]: ") or contact['phone']
            new_email = input(f"New email [{contact['email']}]: ") or contact['email']
            
            contact['name'] = new_name
            contact['phone'] = new_phone
            contact['email'] = new_email

            save_contacts(contacts)
            print("\nContact updated successfully!\n")
            return
    print("\nContact not found.\n")

def delete_contact():
    name_to_delete = input("Enter the name of the contact to delete: ").strip()
    contacts = load_contacts()
    new_contacts = [c for c in contacts if c['name'].lower() != name_to_delete.lower()]
    
    if len(contacts) == len(new_contacts):
        print("\nContact not found.\n")
    else:
        save_contacts(new_contacts)
        print(f"\nContact '{name_to_delete}' deleted successfully.\n")

def main_menu():
    while True:
        print("==== Contact Book Menu ====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.\n")

if __name__ == "__main__":
    main_menu()
