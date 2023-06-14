import xmlrpc.client
import os

def print_response(response):
    print(response)

def call_rpc(function_name, *args):
    try:
        proxy = xmlrpc.client.ServerProxy("http://localhost:5001/")
        response = getattr(proxy, function_name)(*args)
        return response
    except ConnectionRefusedError:
        return "Server is unavailable."
    except AttributeError:
        return f"Method '{function_name}' does not exist."
    except xmlrpc.client.Fault as error:
        return error.faultString

def main():
    while True:
        print("\n--- File System Client Menu ---")
        print("1. Create a file")
        print("2. Read a file")
        print("3. Update a file")
        print("4. Delete a file")
        print("5. List all files")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            filename = input("Enter the filename: ")
            content = input("Enter the file content: ")
            response = call_rpc("create_file", filename, content)
            print_response(response)

        elif choice == "2":
            filename = input("Enter the filename: ")
            response = call_rpc("read_file", filename)
            print_response(response)

        elif choice == "3":
            filename = input("Enter the filename: ")
            content = input("Enter the new file content: ")
            response = call_rpc("update_file", filename, content)
            print_response(response)

        elif choice == "4":
            filename = input("Enter the filename: ")
            response = call_rpc("delete_file", filename)
            print_response(response)

        elif choice == "5":
            response = call_rpc("list_files")
            print_response(response)

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
