s1="Hello World"
# Find out the length of the string
print(len(s1))
# Print the first character of the string s1
print(s1[0])
# Print out the last character of the string s1
print(s1[-1])
# Slice and get the sub-string as 'llo'
print(s1[2:5:1])
# Slice the string and get the substring from s1 and every 2 interval.
print(s1[0::2])
# Slice and save a sub-string in a variable and print its type and output.
sub_string = s1[0:15:3]
print(sub_string)
print(type(sub_string))
# Reverse the string
reverse_string = s1[::-1]
print(reverse_string)