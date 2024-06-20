class FileEditor:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            return "File not found."


    def write_file(self, content):
        with open(self.file_path, 'a') as file:
            file.write(content)
        return "Content written successfully."


if __name__ == "__main__":
    
    editor = FileEditor('names.txt')
    print("Current file content:")
    print(editor.read_file())

    print(editor.write_file('David\nEve\n'))

    print("Updated file content:")
    print(editor.read_file())
