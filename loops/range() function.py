# Print the range of the using only stop
for num in range(5):
    print(num,end=" ")
print(end="\n")
# Print the range of number from 2 to 10 using start, stop
for i in range(2,11):
    print(i,end=" ")
print(end="\n")
# Print the range of number from 1 to 10 with 2 step
for stepping in range(1,11,2):
    print(stepping,end=" ")
print(end="\n")
# Print reverse order from 10 to 1 using range()
for rev in range(10,0,-1):
    print(rev, end=" ")
print(end="\n")
# Convert range into list:
list1 = list(range(0,11))
print(type(list1),list1)
# Convert range into tuple
tuple1 = tuple(range(2,11,2))
print(type(tuple1),tuple1)
