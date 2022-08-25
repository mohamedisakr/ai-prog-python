from statistics import stdev, variance
dataset = [10, 14, 10, 6]

'''
pstdev()    Population standard deviation of data.
pvariance() Population variance of data.
stdev()     Sample standard deviation of data.
variance()  Sample variance of data.
'''

print(f'Sample variance of data: {variance(dataset)}')
print(f'Sample standard deviation of data: {stdev(dataset)}')
