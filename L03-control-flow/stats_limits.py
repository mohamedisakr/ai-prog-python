from statistics import median, mode

Anna = [0, 90, 91, 92, 93, 93, 94]  
Bob = [23, 33, 33, 94, 96, 97, 98]  
Carol = [84, 85, 86, 87, 88, 88, 89]  
Doug = [2, 3, 11, 14, 21, 100, 100]  

anna_average = sum(Anna)/len(Anna)
print(f'Anna Average: {anna_average}')

bob_average = sum(Bob)/len(Bob)
print(f'Bob Average: {bob_average}')

carol_average = sum(Carol)/len(Carol)
print(f'Carol Average: {carol_average}')


doug_average = sum(Doug)/len(Doug)
print(f'Doug Average: {doug_average}')

print()
print(f'Anna Median: {median(Anna)}')
print(f'Bob Median: {median(Bob)}')
print(f'Carol Median: {median(Carol)}')
print(f'Doug Median: {median(Doug)}')

print()
print(f'Anna Mode: {mode(Anna)}')
print(f'Bob Mode: {mode(Bob)}')
print(f'Carol Mode: {mode(Carol)}')
print(f'Doug Mode: {mode(Doug)}')
