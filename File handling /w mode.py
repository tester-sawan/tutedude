# w mode is used to open a file in write mode. This will overwrite the existing file.
# As we open the file in w mode, the content of the file will be deleted and ready for overwriting.
openfile=open("file1.txt","wt")
openfile.write("This file is overwritten using the w modes.\n")
openfile.write("Have a great day.")
openfile.close()