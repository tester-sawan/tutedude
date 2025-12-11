#Method-1:
sample_file = open("/home/adventus-user/Documents/external_file.txt","rt")
for line in sample_file:
    print(line)
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