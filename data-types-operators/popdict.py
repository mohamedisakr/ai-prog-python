population = {
    'Shanghai':	17.8,
    'Istanbul':	13.3,
    'Karachi':	13.0,
    'Mumbai':	12.5,
}

country = 'Berlin'
print(population.get(country, f'{country} is not in the list'))


a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a == b)
print(a is b)
print(a == c)
print(a is c)
