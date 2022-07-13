#Module for Converting Temperatures


#(32°F − 32) × 5/9 = 0°C
def convertCelsius(temperature):
    float((temperature - 32) * (5/9))
    return

#(32°C × 9/5) + 32 = 89.6°F
def convertFahrenheit(temperature):
    float((temperature * (9/5)) + 32)
    return
