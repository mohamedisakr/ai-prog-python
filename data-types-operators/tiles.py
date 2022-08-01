# Fill this in with an expression that calculates how many tiles are needed.


from math import ceil


def CalculateTiles():
    # One part is 9 tiles wide by 7 tiles long,
    # the other is 5 tiles wide by 7 tiles long.
    # Tiles come in packages of 6.
    first = 9 * 7
    second = 5 * 7
    package = 6
    tiles = ((first+second) / package)
    return tiles


result = CalculateTiles()
print(result)

# Fill this in with an expression that calculates how many tiles will be left
# over.
print(ceil(result)-result)
