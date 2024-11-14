###
# A program that checks if the speed of a vehicle on a highway is between 40 and 140 km/h
speed = int(input('Enter the speed of the car in km/h: '))
is_speed = speed >= 40 and speed <= 140
print(f'Speed is valid: {is_speed}')