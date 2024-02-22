def steak_point():
    temperature = int(input('What is the temperature of the steak? '))

    if temperature in range(48, 53):
        print(f'At a temperature of {temperature}ºF, the steak is rare.')
    
    elif temperature in range(54, 59):
        print(f'At a temperature of {temperature}ºF, the steak is medium-rare.')

    elif temperature in range(60, 64):
        print(f'At a temperature of {temperature}ºF, the steak is medium.')

    elif temperature in range(65, 70):
        print(f'At a temperature of {temperature}ºF, the steak is medium-well.')
    
    elif temperature in range(71, 75):
        print(f'At a temperature of {temperature}ºF, the steak is well done.')

    elif temperature > 75:
        print(f'At a temperature of {temperature}ºF, the steak is burnt.')

    else:
        print(f'At a temperature of {temperature}ºF, the steak is raw.')



    






