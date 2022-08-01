def calculateAverage(bills):
    total = 0
    for item in bills:
        total += item
        # print(item)
    return total


bills = [23, 32, 64]
print(calculateAverage(bills))
