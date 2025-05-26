def write_file(file_name, file_content):
    file_name = str(file_name) + ".txt"
    with open(file_name, 'w') as f:
        f.write(file_content)

def append_file(file_name, append_content):
    file_name = str(file_name) + ".txt"
    with open(file_name, "a") as file:
        file.write(append_content)

def read_file(file_name):
    file_name = str(file_name) + ".txt"
    with open(file_name, "r") as f:
        return f.read()