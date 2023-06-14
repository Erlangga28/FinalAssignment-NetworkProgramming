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
        print("create_file")
        print("read_file")
        print("update_file")
        print("delete_file")
        print("list_file")
        print("exit")
        choice = input("Enter your command: ")

        if choice == "create_file":
            filename = input("Enter the filename: ")
            content = input("Enter the file content: ")
            response = call_rpc("create_file", filename, content)
            print_response(response)

        elif choice == "read_file":
            filename = input("Enter the filename: ")
            response = call_rpc("read_file", filename)
            print_response(response)

        elif choice == "update_file":
            filename = input("Enter the filename: ")
            content = input("Enter the new file content: ")
            response = call_rpc("update_file", filename, content)
            print_response(response)

        elif choice == "delete_file":
            filename = input("Enter the filename: ")
            response = call_rpc("delete_file", filename)
            print_response(response)

        elif choice == "list_file":
            response = call_rpc("list_files")
            print_response(response)

        elif choice == "exit":
            break

        else:
            print("Invalid command. Please try again.")

if __name__ == '__main__':
    main()
