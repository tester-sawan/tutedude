with open("/home/adventus-user/Documents/external_file.txt","rt") as file:
    content = file.read()
    print(content)
with open("/home/adventus-user/Documents/external_file1.txt","wt") as new_file:
    content=new_file.write("This is a new file.")
