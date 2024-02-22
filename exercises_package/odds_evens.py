def odds_evens():
    initial_number = int(input("what's the initial number of the list? "))
    final_number = int(input("what's the final number of the list? "))
    even = []
    odd=[]

    for number in range(initial_number, final_number):
        if number % 2==0:
            even.append(number)
        else:
            odd.append(number)
    print(f"The even numbers of the range are: {even}")
    print(f"The odd numbers of the range are: {odd}")


