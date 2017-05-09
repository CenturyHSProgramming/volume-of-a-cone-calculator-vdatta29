# ConeVolumeCalculator.py
# Your job is to write a function in ConeVolumeCalculator.py (call
# it **calculateConeVolume()** that calculates the volume of a cone
# factor based on the Volume Calculator
# Calculator.net (http://www.calculator.net/volume-calculator.html)


# Define Function below
# be sure to return an integer

import math

def calculateConeVolume(baseRadius, height):
    calculateConeVolume = (1/3) * math.pi * baseRadius**2 * height
    calculateConeVolume = round(float(calculateConeVolume), 2)
    return(calculateConeVolume)
    
    



if __name__ == '__main__':
    # Call the function in here if you want to test it
    # Make sure it's indented
    baseRadius = float(input('Enter the raduis of the cone:    '))
    height =  float(input('Enter the height of the cone:    '))
    volume = calculateConeVolume(baseRadius, height)
    print(volume)
    
