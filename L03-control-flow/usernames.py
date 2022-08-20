# 13. Quiz: For Loops
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
# for name in names:
#     usernames.append(name.lower().replace(" ", "_"))

for index in range(len(names)):
    usernames.append(names[index].lower().replace(" ", "_"))

# usernames = ["joey_tribbiani", "monica_geller", "chandler_bing",
#               "phoebe_buffay"]
print(usernames)
