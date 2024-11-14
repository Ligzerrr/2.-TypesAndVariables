###
# The program calculates the cost of transporting goods
# based on the given distance in km, fuel price per 1 liter,
# and fuel consumption in liters per 100 km.
#
distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input('Enter the amount of fuel used per 100 km: '))
total_fuel_consumption = fuel_consumption * (distance / 100)
total_cost = fuel_price * total_fuel_consumption
print(f'The total fuel consumption amounts to: {total_fuel_consumption}.')
print(f'The total cost of all the fuel is: {total_cost}.')