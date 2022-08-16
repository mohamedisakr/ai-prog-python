# Find the largest integer that is less than 1000,
# two more than a multiple of 3,
# two more than a multiple of 5,
# odd.
def find_number():
    for i in range(999, 0, -2):
        if(i % 3 == 2 and i % 5 == 2):
            print(i)


find_number()
