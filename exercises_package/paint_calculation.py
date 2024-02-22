def paint_calculation():
    coverage = int(input('What is the coverage in square meters of your paint can? '))
    height = int(input('What is the height in meters of your wall? '))
    length = int(input('What is the length in meters of your wall? '))

    return print(f'You need {(height * length) / coverage} cans of paint to paint your wall.')



