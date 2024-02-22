def whats_the_capital():

    cities = {
        'brazil': 'brasilia',
        'argentina': 'buenos Aires',
        'chile': 'santiago',
        'australia': 'canberra',
        'canada': 'ottawa'
    }

    user_country = input('Enter the name of the country: ').lower()

    if user_country in cities:
        print(f"The caital of {user_country} is {cities[user_country]}")

    else:
        print(f"There are no informations aboute {user_country}")


