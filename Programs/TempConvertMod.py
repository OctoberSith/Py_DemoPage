#Module for Converting Temperatures


#(32°F − 32) × 5/9 = 0°C
def convertCelsius(temperature):
    return float((temperature - 32) * (5/9))
    

#(32°C × 9/5) + 32 = 89.6°F
def convertFahrenheit(temperature):
    return float((temperature * (9/5)) + 32)
    
