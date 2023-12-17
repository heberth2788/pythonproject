from io import TextIOWrapper

# Opening a file
file_name = "/Users/heberthdeza/Files/myTestFile.txt"
mode = "r"
fileDesc: TextIOWrapper = open(file = file_name, mode = mode)

# Reading the file
print(fileDesc.readline())
for line in fileDesc:
     print(line)
fileDesc.seek(0) # Move the file descriptor pointer to the beginning of the file.
print(fileDesc.read())
print(fileDesc.closed)
fileDesc.close() # Close the file, always the file should be closed at the end.
print(fileDesc.closed)

# Writing the file
mode = "a+" # "a+" mode to add(a) and read(+) the file.
fileDesc = open(file = file_name, mode = mode)
fileDesc.write("This is a new line\n")
textLines = ["line1\n", "line2\n", "line3\n"]
fileDesc.writelines(textLines)
fileDesc.seek(0)
print("------\n", fileDesc.read())
fileDesc.close()


