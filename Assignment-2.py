def getWeight():
    weight = float(input("Weight in pounds: "))
    weight = weight*0.45
    return weight

def getHeight():
    height = float(input("Height in inches: "))
    height = height*0.025
    return height

def calculate(weight, height):
    height = height**2
    BMI = weight/height
    return round(BMI,1)

def verdict(BMI):
    if BMI < 18.5:
        print("BMI: " + str(BMI) + "\nUser is Under weight")
    elif BMI <= 24.9:
        print("BMI: " + str(BMI) + "\nUser is Normal weight")
    elif BMI <= 29.9:
        print("BMI: " + str(BMI) + "\nUser is Overweight")
    else:
        print("BMI: " + str(BMI) + "\nUser is Obese")

def Main():
    weight = getWeight()
    height = getHeight()
    BMI = calculate(weight, height)
    verdict(BMI)

Main()