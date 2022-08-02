# '''
# You decide you want to play a game where you are hiding
# a number from someone.
# Store this number in a variable called 'answer'.
# Another user provides a number called# 'guess'.
# By comparing guess to answer, you inform the user
# if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
# '''
answer = 100  # provide answer
guess = 100  # provide guess

if guess < answer:
    result = "Oops!  Your guess was too low."
elif guess > answer:
    result = "Oops!  Your guess was too high."
elif guess == answer:
    result = "Nice!  Your guess matched the answer!"
print(result)


print(result)

###############################

# '''
# Depending on where an individual is from we need to tax them
# appropriately.  The states of CA, MN, and
# NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and
# the corresponding state to assure that they are taxed by the right
# amount.
# '''

CA_TAX = 0.075  # 7.5/100
MN_TAX = 0.095  # 9.5/100
NY_TAX = 0.089  # 8.9/100
MSG = "Since you're from {}, your total cost is {}."
state = 'NY'  # Either CA, MN, or NY
purchase_amount = 200  # amount of purchase

if state == 'CA':  # provide conditional for checking state is CA
    total_cost = purchase_amount * (1+CA_TAX)
    result = MSG.format(state, total_cost)
elif state == 'MN':  # provide conditional for checking state is MN
    total_cost = purchase_amount*(1+MN_TAX)
    result = MSG.format(state, total_cost)
elif state == 'NY':  # provide conditional for checking state is NY
    total_cost = purchase_amount*(1+NY_TAX)
    result = MSG.format(state, total_cost)

print(result)
