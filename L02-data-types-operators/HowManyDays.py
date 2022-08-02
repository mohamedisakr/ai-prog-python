month = 8
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# use list indexing to determine the number of days in month
num_days = days_in_month[month-1]


print(num_days)


eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']


# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[-3:])

# Match the Python code below with the value of the modified sentence1
# or sentence2. If the code results in an error, match it with “Error”.

sentence1 = "I wish to register a complaint."
sentence2 = ["I", "wish", "to", "register", "a", "complaint", "."]

sentence2[6] = "!"
print(sentence2)

sentence2[0] = "Our Majesty"
print(sentence2)

sentence2[0:2] = ["We", "want"]
print(sentence2)

sentence1[30] = "!"
print(sentence1)
