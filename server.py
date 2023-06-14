import os
from xmlrpc.server import SimpleXMLRPCServer

class FileSystemServer:
    def __init__(self):
        self.base_path = os.getcwd() + '/files/'  # Directory to store files

    def create_file(self, filename, content):
        file_path = os.path.join(self.base_path, filename)
        with open(file_path, 'w') as file:
            file.write(content)
        return f"File '{filename}' created successfully."

    def read_file(self, filename):
        file_path = os.path.join(self.base_path, filename)
        if not os.path.isfile(file_path):
            return f"File '{filename}' does not exist."
        with open(file_path, 'r') as file:
            return file.read()

    def update_file(self, filename, content):
        file_path = os.path.join(self.base_path, filename)
        if not os.path.isfile(file_path):
            return f"File '{filename}' does not exist."
        with open(file_path, 'w') as file:
            file.write(content)
        return f"File '{filename}' updated successfully."

    def delete_file(self, filename):
        file_path = os.path.join(self.base_path, filename)
        if not os.path.isfile(file_path):
            return f"File '{filename}' does not exist."
        os.remove(file_path)
        return f"File '{filename}' deleted successfully."

    def list_files(self):
        files = os.listdir(self.base_path)
        return files

# Create server and register functions
server = SimpleXMLRPCServer(("localhost", 5001))
server.register_instance(FileSystemServer())

# Start the server
print("Server started")
server.serve_forever()
