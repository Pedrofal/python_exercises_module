def numbers_in_range():
    while True:
        inicial_number = input("What's the initial number to the range? ")
        final_number = input("What's the final number to the range? ")
        
        try:
            inicial_number = int(inicial_number)
            final_number = int(final_number) + 1
            break  
        except ValueError:
            print("Add a valid number")

    
    for number in range(inicial_number, final_number):
        print(number)


