# If the file not found, it will create a file with the name given as argument.
file_handler = open("file1.txt","xt")
# Write something into the file, we have write() function. As this is a text file, we can store value as string.
file_handler.write("Welcome to the python learning.\nThis file is created by the x mode.")
# Close the file
file_handler.close()


