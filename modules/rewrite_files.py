import os, pathlib

"""" Simple function just to reorder the csv-file"""

#auxiliary function to do the repeated task
  
def writeLines(counter,fileName):
    for line in fileName:
     if line.endswith(f',{counter}\n'):
        #print('Function executing:', counter)
        with open('work4_2_sorted.csv', 'a') as file1:
            #print("Line generated")
            file1.write(f"{line}\n")
    return None

def rewriteFiles():
  
    file_path = (pathlib.Path(__file__).parent)
    file_path = file_path.parent
#print(file_path)
    new_path = f'{file_path}'+'\\work4part_2.csv'
#print(new_path)

    for i in range(5):
        with open(new_path,'r') as file:
            fileName = file
            writeLines(i,fileName)

    return print('Files sorted!')
    