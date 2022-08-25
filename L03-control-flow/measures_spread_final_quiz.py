from statistics import mean, median, mode, stdev, variance

quiz_7 = [2, 3, 3, 3, 4, 6, 7, 8, 9, 12, 15, 15, 22]

n = len(quiz_7)
print(f'dataset length: {n}')

median = median(quiz_7)
print(f'dataset median: {median}')

mean = mean(quiz_7)
print(f'dataset mean: {mean}')

mode = mode(quiz_7)
print(f'dataset mode: {mode}')


# median
# first quartile
# third quartile
# mean
# mode
print('-------------------------------------')

quiz_8 = [2, 3, 3, 3, 4, 6, 7, 8, 9, 12, 15, 15, 22]
# interquartile range
# minimum
minimum = min(quiz_8)
print(f'dataset min: {minimum}')

# maximum
maximum = max(quiz_8)
print(f'dataset max: {maximum}')

# range
theRange = maximum-minimum
print(f'dataset range: {theRange}')

# variance
var = variance(quiz_8)
print(f'dataset variance: {var}')

# standard deviation
stdDev = stdev(quiz_8)
print(f'dataset standard deviation: {stdDev}')
