#!/usr/bin/env python
import ADC0832
import time
import math

# Constants for the thermistor characteristics
R0 = 10000  # Resistance at a known temperature (in ohms)
T0 = 25     # Known temperature in Celsius (adjust as needed)
B = 3950    # Beta coefficient of the thermistor (adjust as needed)

def init():
    ADC0832.setup()

def temperature_from_resistance(Rt):
    # Calculate temperature in Celsius using the Steinhart-Hart equation
    inv_T = 1.0 / (T0 + 273.15) + (1.0 / B) * math.log(Rt / R0)
    temperature_C = 1.0 / inv_T - 273.15
    return temperature_C

def loop():
    while True:
        res = ADC0832.getADC(0)
        Vr = 3.3 * float(res) / 255
        Rt = 10000 * Vr / (3.3 - Vr)
        
        temperature_C = temperature_from_resistance(Rt)
        temperature_F = (temperature_C * 9/5) + 32  # Convert to Fahrenheit

        print(f'Temperature (Celsius): {temperature_C:.2f}°C')
        print(f'Temperature (Fahrenheit): {temperature_F:.2f}°F')

        time.sleep(0.2)

if __name__ == '__main__':
    init()
    try:
        loop()
    except KeyboardInterrupt:
        ADC0832.destroy()
        print('The end!')
