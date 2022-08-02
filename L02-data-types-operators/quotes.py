# TODO: Fix this string!
ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'
print(ford_quote)

coconut_count = "34"
mango_count = "15"
tropical_fruit_count = coconut_count + mango_count
print(tropical_fruit_count)

username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."
message = username + ' accessed the site ' + url + ' at ' + timestamp
print(message)


given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

# todo: calculate how long this name is
name_length = len(given_name)+len(middle_names)+len(family_name)+2

# Now we check to make sure that the name fits within the driving license
# character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(f'full name length {name_length}')
print(name_length <= driving_license_character_limit)

# print(len(835))
