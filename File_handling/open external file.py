#Method-1:
sample_file = open("/home/adventus-user/Documents/external_file.txt","rt")
file_read = sample_file.readlines()
print(file_read)
print(file_read[0])
print("elcome to the python programming language.\n" in file_read)
print(type(file_read))
for line in file_read:
    print(line.rstrip('\n'))
# file_read1 = sample_file.readline()
# file_read2 = sample_file.readline()
# print(file_read1)
# print(file_read2)

# for line in sample_file:
#     print(line)
# Method -2:
# with open("/home/adventus-user/Documents/external_file.txt","rt") as f:
#     for line in f:
#         print(line)
# # print(sample_file)
# # readFile = sample_file.read()
# # print(readFile)
# #sample_file.close()
# # Can we use the loop the sample file as read mode
sample_file.close()