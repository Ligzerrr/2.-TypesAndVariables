### 3.1
#7 variables

company = "ABC Data" #name: company value: "ABC DATA" type: str
phone = "555-123-009" #name: phone value: "555-123-009" type: str
employees = 25 #name: employees value: 25 type: int
remote_work = True #name: remote_work value: true type: bool
big_company = employees > 100 #name: big_company value: false type: bool
income = 4500000 #name: income value: 4500000 type: int
income_per_person = income / employees #name: income_per_person value: 180,000 type: int   

### 3.2
# A program that calculates the sum of two numbers.
# Modify the program to calculate the sum of three numbers.
#
number1 = 71 #liczba1 liczba2 liczba3
number2 = 14
number3 = 53
result = number1 + number2 + number3 #suma liczb
print('Number 1: ', number1) #wyswietlenie wszystkich liczb od poczatku
print('Number 2: ', number2)
print('Number 3: ', number3)
print('The result of summation: ', result) #wyswietlenie sumy liczb

### 3.3
# A program for swapping two varable values
#
x = 7
y = 34
z = 0 # additional, auxiliary variable
print("Before swapping: x=", x, "y=", y) #wyswietlenie liczb

# swap the values
z = y #z = 34, dzięki czemu przy przypisaniu do y wartości z x, zapamiętana jest liczba 34
y = x
x = z
print("After swapping: x=", x, "y=", y)

### 3.4
# A program that, for a given speed in km/h,
# prints the speed in m/s
#
speed_kmh = 70
speed_ms = speed_kmh / 3.6 #Zamiana z kmh na metry na sekunde (dzieli sie przez 3.6)
print(speed_kmh, "km/h = ", speed_ms, "m/s")

### 3.5
# A program that calculates the length of the diagonal
# of a rectangle with sides a and b.
#
import math
a = 5
b = 8
diagonal = math.sqrt(a**2 + b**2) #twierdzenie pitagorasa
print(diagonal)
### 3.6
# A program that calculates the distance to horizon depending on the height of the observer above ground
import math #biblioteka math do sqrt
h = input('Enter your height in meters: ')
h = float(h)
d = 3.57 * math.sqrt(h) #to z tego wzoru co był w zadaniach
print("When you are standing on the beach the horizon is only", d ,"kilometers away.")
windowheight = 20
dwin = 3.57 * math.sqrt(windowheight)
print("When you are looking out of a window placed 20 meters above the ground the horizon is" ,round(dwin,4), "kilometers away.")

### 3.7
# A program that calculates and prints:
# - the number of people and percentage of the total
#   population living in the Northern Hemisphere
# - the number of people and percentage of the total
#   population living in the Southern Hemisphere
#
total = 8000000000
north = 7200000000
south = total - north
print("World population: ", total)
print("Northern Hemisphere: ", north)
print("Northern Hemisphere in %: ", north/total*100)
print("Southern Hemisphere: ", south)
print("Southern Hemisphere in %: ", south/total*100)

### 3.8
# A program that calculates and prints
# the average grade of a student
#
math = 5
art = 4
music = 5
history = 3
average = (math + art + music + history) / 4
print("Average grade is", average)

