#BMI Logic

def bmiLogic(weight, height):
    BMI = (weight * 703)/(pow(height, 2))
    classification = ""
    healthRisk = ""
    diagnosis =""

    if(BMI < 18.5):
        classification += "Underweight"
        healthRisk += "Minimal"
        diagnosis += "Eat Something Fool!"
    elif(BMI >= 18.5 and BMI <= 24.9):
        classification += "Normal Weight"
        healthRisk += "Minimal"
        diagnosis += "You are fine. Have fun."
    elif(BMI > 25 and BMI <= 29.9):
        classification += "Overweight"
        healthRisk += "Increased"
        diagnosis += "Walk it off, Fatty."
    elif(BMI > 30 and BMI <= 34.9):
        classification += "Obese"
        healthRisk += "High"
        diagnosis += "Christ, I can hear you getting fatter!"
    elif(BMI > 35 and BMI <= 39.9):
        classification += "Severly Obese"
        healthRisk += "Very High"
        diagnosis += "Time to sell all that stock in Krispy Kreme."
    elif(BMI > 40):
        classification += "Morbidly Obese"
        healthRisk += "Extremely High"
        diagnosis += "They arent going to be afford the coffin size for your funeral."
    print("============================")
    print("")
    print("Your Weight: " + str(weight))
    print("Your Height: " + str(height))
    print("")
    print("============================")
    print("")
    print("Your Results:")
    print("")
    print("BMI: " + str(BMI))
    print("Classification: " + classification)
    print("Health Risk: " + healthRisk)
    print("Diagnosis: " + diagnosis)
    print("")
    print("============================")
    input("Press enter to Close Program")
    return 