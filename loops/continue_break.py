# The continue statement is used to skip the current iteration and move to the next iteration of the loop. It is used when we want to skip specific value but continue the loop.
# Write a programme to print only even number using the continue statement.
for i in range(11):
    if i%2!=0:
        continue
    print(i)
# Break statement is used to exist from a loop immediately in case certain condition as specified is true.
for i in range(10):
    if i==6:
        break
    print(i)