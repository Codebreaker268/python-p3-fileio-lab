def write_file(file_name, file_content):
    with open(f"{file_name}.txt",mode='w') as file:
        file.write(file_content)


def append_file(file_name, append_content):
    with open(f"{file_name}.txt",mode='a')as item:
        item.write(append_content)
    pass

def read_file(file_name):
    with open(f"{file_name}.txt",mode='r') as sth:
        return sth.read()
