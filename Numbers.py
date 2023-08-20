# Write a function, 
# which takes three integers a, b, and c as arguments, 
# and returns True if exactly two of of the three integers are positive numbers (greater than zero), 
# and False - otherwise.

def positive(a, b, c):
    count = 0

    if a > 0:
        count += 1
    if b > 0:
        count += 1
    if c > 0:
        count += 1

    return count == 2

print(positive(4, 0, 2))



