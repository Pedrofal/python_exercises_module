def filter_employees():
    employees = ['ana', 'amanda', 'marcos', 'joaquim', 'lurdes', 'josefa', 'mariano', 'maria']
    night_shift = ['amanda', 'marcos', 'joaquim', 'lurdes']
    day_shift = ['ana', 'josefa', 'mariano', 'maria']
    has_car = ['amanda', 'marcos', 'maria', 'josefa']

    car_at_night = set(night_shift).intersection(has_car)
    print(f'Employees who have a car and work at night: {car_at_night}')

    car_at_day = set(day_shift).intersection(has_car)
    print(f'Employees who have a car and work during the day: {car_at_day}')

    without_car = set(employees).difference(has_car)
    print(f'Employees who do not have a car: {without_car}')




