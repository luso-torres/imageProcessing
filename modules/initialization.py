import os

def initialize(line_to_append,file_name):
    print("File initialized")
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            content = file.read()  # Read the content of the file

        if content.__contains__(line_to_append):
            print(f"Line already exists in {file_name}")
            return  # Exit if the line already exists
    else:
        # If the file doesn't exist, it will be created when we append
        print(f"{file_name} does not exist. It will be created.")
        with open(file_name,"a") as file:
            file.write(line_to_append+'\n')

    return