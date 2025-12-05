# for i in range(3):
#     for j in range (2):
#         print(i,j)

"""
Print the following start pattern in console
*
**
***
****
*****
"""
row_count = 1
for i in range(1,6):
    for j in range(i):
        print("*", end=" ")
    print()
print("This program ends here.")


