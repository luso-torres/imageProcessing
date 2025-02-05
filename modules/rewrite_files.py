import os, pathlib

"""" Simple function just to reorder the csv-file"""

#auxiliary function to do the repeated task
  
def writeLines(counter,file_unsorted,file_name):
    for line in file_unsorted:
     #print('Function executing:', line,'\n')
     if line.endswith(f',{counter}\n'):
        #print('Function executing:', counter)
        with open(f'{file_name}', 'a') as file1:
            #print("Line generated")
            file1.write(f"{line}")
    return None

def rewriteFiles(file_unsorted,file_name):
  
    file_path = (pathlib.Path(__file__).parent)
    file_path = file_path.parent
#print(file_path)
    new_path = f'{file_unsorted}'
    #print(new_path)

    with open(new_path,'r') as file:
            fileLines = file.readlines()
    for i in range(5):
        writeLines(i,fileLines,file_name)
        #print("Writing Line ",i)

    return print('Files sorted!')
    