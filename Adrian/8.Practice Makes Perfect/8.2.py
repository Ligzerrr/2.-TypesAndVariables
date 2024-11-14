###
# Calculation of area and circumference of a circle

radius = int(input('Enter the radius of the circle: '))
PI = 3.14 #Można użyć math.pi z biblioteki math
area = PI * radius**2
circumference = PI * radius * 2
print(f'The area of a circle with the radius: {radius} is: {area} and the circumference of the circle is equal to: {circumference}')
