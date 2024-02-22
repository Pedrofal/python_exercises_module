def bmi_calculator():
    weight = float(input("What's your weight in Kg? "))
    height = float(input("What's your height in centimeters? "))
    bmi = weight / (height / 100) ** 2

    if bmi < 18.5:
        print(f'Your BMI is {bmi}, you are underweight.')
    elif 18.5 <= bmi <= 24.9:
        print(f'Your BMI is {bmi}, you are at a healthy weight.')
    elif 25 <= bmi <= 29.9:
        print(f'Your BMI is {bmi}, you are overweight.') 
    elif 30 <= bmi <= 39.9:
        print(f'Your BMI is {bmi}, you are obese.')  
    elif bmi <= 40:
        print(f'Your BMI is {bmi}, you are severely obese.')    


