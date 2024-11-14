###
# A program that prints the number of dice rolled and the value True if the number rolled is 1 or 6

import random
number = random.randint(1,6)
is_special = number == 1 or number == 6
print(f'The number rolled is: {number}.')
print(f'The number is special: {is_special}.')
                