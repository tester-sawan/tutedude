# read() function is used to read the file.
#Step-1: Open the file
open_file = open("file1.txt","rt")
#Step-2: Read the open file using read():
read_content = open_file.read()
#Step-3: show the content.
print(read_content)
#Step-4: Close the file
open_file.close()