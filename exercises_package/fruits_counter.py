def fruits_counter():
    fruits = ['apple', 'banana', 'orange', 'banana', 'strawberry', 'grape', 'banana']
    count = 0
    fruit=input("Enter the name of the fruit that you want to check the quantity: ").lower()

    for item in fruits:
        if item == fruit:
            count += 1

    if count > 0:
        if count > 1:
            print(f"There are {count} '{fruit}s' in the list of fruits")
        else:
            print(f"There is {count} '{fruit}' in the list of fruits")
    else:
        print(f"There are no '{fruit}'s in the list of fruits")



