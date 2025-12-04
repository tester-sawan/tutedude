scores = [2,45,102,4,9,12,45,90,1,0,1]
# Find the minimum score from a list.
min_score = scores[0]
max_score = scores[0]
total_score = 0
for i in range(len(scores)):
    if scores[i] <= min_score:
        min_score = scores[i]
print(f"The minimum score available under a list 'scores' is {min_score}.")

# Find the maximum score from a list
for i in range(len(scores)):
    if scores[i]>=max_score:
        max_score=scores[i]
print(f"The maximum scores available under a list 'scores' is {max_score}.")

# Final the total count of all scores available under a list.
for i in range(len(scores)):
    total_score = total_score+scores[i]
print(f"The total count of all the available scores in  the list is: {total_score}.")