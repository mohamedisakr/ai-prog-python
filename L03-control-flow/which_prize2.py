points = 40  # 174  # use this as input for your submission

# establish the default prize value to None
prize = None
# result = ''

# write your if statement here
if points >= 1 and points <= 50:
    prize = 'wooden rabbit'
    result = f"Congratulations! You won a {prize}!"
elif points >= 51 and points <= 150:
    result = "Oh dear, no prize this time."
elif points >= 151 and points <= 180:
    prize = 'wafer-thin mint'
    result = f"Congratulations! You won a {prize}!"
elif points >= 181 and points <= 200:
    prize = 'penguin'
    result = f"Congratulations! You won a {prize}!"
else:
    result = 'points can only take on positive integer values up to 200.'

print(result)


# use the points value to assign prizes to the correct prize names


# use the truth value of prize to assign result to the correct prize


# print(result)
