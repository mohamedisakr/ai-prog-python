mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"


sales = [121,
         105,
         110,
         98,
         95]
total = 0

for sale in sales:
    total += sale

# TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.
print(f'This week\'s total sales: {total}')
