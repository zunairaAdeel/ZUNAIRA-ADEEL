import pyspark
def save_task(task):
    with open('tasks.txt', 'a') as file:
        file.write(task + '\n')

def display_tasks():
    with open('tasks.txt', 'r') as file:
        tasks = file.readlines()
        if tasks:
            print("Tasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task.strip()}")
        else:
            print("No tasks saved.")

def main():
    while True:
        print("\nTask Manager")
        print("1. Add a task")
        print("2. Display tasks")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            task = input("Enter a task: ")
            save_task(task)
            print("Task saved successfully!")
        elif choice == '2':
            display_tasks()
        elif choice == '3':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

def save_data(data):
     with open('data.txt', 'a') as file:
        file.write(data + '\n')

def display_data():
    with open('data.txt', 'r') as file:
        data = file.readlines()
        if data:
            print("Data:")
            for idx, d in enumerate(data, start=1):
                print(f"{idx}. {d.strip()}")
        else:
            print("No data saved.")

def main():
    while True:
        print("\nData Processor")
        print("1. Add data")
        print("2. Display data")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            data = input("Enter data: ")
            save_data(data)
            print("Data saved successfully!")
        elif choice == '2':
            display_data()
        elif choice == '3':
            print("Exiting Data Processor.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 

def write_to_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)

def show_all_files():
    import os
    files = os.listdir('.')
    print("Files available:")
    for idx, file_name in enumerate(files, start=1):
        print(f"{idx}. {file_name}")

def view_file_content(file_name):
    try:
        with open(file_name, 'r') as file:
            print(f"Content of '{file_name}':")
            print(file.read())
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

def main():
    while True:
        option = input("Choose an option:\n1. Write to a file\n2. Show all files\n3. View file content\n4. Exit\n")

        if option == '1':
            file_name = input("Enter file name: ")
            content = input("Enter content: ")
            write_to_file(file_name, content)
            print("File has been written successfully!\n")
        elif option == '2':
            show_all_files()
        elif option == '3':
            file_name = input("Enter the file name to view its content: ")
            view_file_content(file_name)
        elif option == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid option. Please choose again.\n")

if __name__ == "__main__":
    main()