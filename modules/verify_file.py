import os
import numpy as np


def verifyFile(line,number,file_name) -> None:
    line_to_append = f'{line},{number}'

    # Read the content of the file if it exists
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            content = file.read()  # Read the content of the file

        if line_to_append in content:
            print(f"Line already exists in {file_name}")
            return  # Exit if the line already exists
    else:
        # If the file doesn't exist, it will be created when we append
        print(f"{file_name} does not exist. It will be created.")

    # Append the line to the file if it's not already in the content
    with open(file_name, "a") as file:
        file.write(",".join(map(str, line)) + f',{number}\n')  # Write the new line to the file
        #print(f"Line appended to {file_name}")
    return None