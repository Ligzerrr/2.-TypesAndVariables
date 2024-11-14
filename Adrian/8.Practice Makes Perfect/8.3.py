###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

celsius = float(input('Enter the value in degrees Celsius: ')) #Float ponieważ inne stopnie bedą podawane z liczbami po przecinku
fahrenheit = round((celsius * 1.8) + 32, 2) #Stopnie celsiusza zamienia sie na fahrenheity za pomoca wzoru: *F = (*C * 9/5) + 32.   Zaokrąglenie aby uniknąć niepotrzebnych znaków
kelvin = round(celsius + 273.15, 2) #Stopnie celsiusza zamienia sie na kelviny dodajac 273.15 (0*C = 273.15 K)
print(f'{celsius} degrees Celsius is: {fahrenheit} degrees Fahrenheit and: {kelvin} degrees Kelvin')