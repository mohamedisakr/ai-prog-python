'''
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for city in cities:
    print(city.title())
print("Done!")

new_cities = []

for city in cities:
    new_cities.append(city.title())
print(new_cities)
'''
# for num in (range(1, 10, 2)):
#     print(num)

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']

for index in range(len(cities)):
    print(cities[index].title())
