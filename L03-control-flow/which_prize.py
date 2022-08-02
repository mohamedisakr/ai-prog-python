# use this input to make your submission

points = -1  # 174  # 500
result = ''

# write your if statement here
if points >= 1 and points <= 50:
    result = "Congratulations! You won a [wooden rabbit]!"
elif points >= 51 and points <= 150:
    result = "Oh dear, no prize this time."
elif points >= 151 and points <= 180:
    result = "Congratulations! You won a [wafer-thin mint]!"
elif points >= 181 and points <= 200:
    result = "Congratulations! You won a [penguin]!"
else:
    result = 'points can only take on positive integer values up to 200.'

print(result)

'''

points = 500  # 174

if points <= 50:
    result = "Congratulations! You won a wooden rabbit!"
elif points <= 150:
    result = "Oh dear, no prize this time."
elif points <= 180:
    result = "Congratulations! You won a wafer-thin mint!"
else:
    result = "Congratulations! You won a penguin!"

print(result)

'''
