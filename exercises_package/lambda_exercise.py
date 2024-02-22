def lambda_exercise():
    number = int(input("What number do you want to know if is even or odd? "))
    even_or_odd = lambda number: 'even' if number%2 == 0 else 'odd'
    print(f"The number {number} is {even_or_odd(number)}")




