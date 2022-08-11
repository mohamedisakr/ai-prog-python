avg = 54.5
heights = [53, 53, 53, 54, 54, 54, 55, 56, 56, 57]
total_up = 0
total_down = 0

for hi in heights:
    if hi > avg:
        total_up += hi - avg
    if hi < avg:
        total_down += avg-hi

# print(total_up)
# print(total_down)

# tests = [82, 82, 82, 82, 82, 82, 82]
# print(tests)

# numbers = [1, 2, 3, 4, 5]
# multiplied = [number * 2 for number in numbers]

bags = [6,  8,  12,  14,  15]
new_bags = [x + 23 for x in bags]
print(new_bags)
