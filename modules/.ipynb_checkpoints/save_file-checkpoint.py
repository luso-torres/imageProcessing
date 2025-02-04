def saveFile(data,folderNumber) -> None:

    with open("files-generated.csv", "w") as file:
        file.write(f'{data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}, {data[5]}, {data[6]}, {data[7]}, {folderNumber} ')