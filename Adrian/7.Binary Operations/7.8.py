###
# A program that prints results of three dice rolls
# and the sum of dice rolled.
#
import random
dice_roll_1 = random.randint(1,6)
dice_roll_2 = random.randint(1,6)
dice_roll_3 = random.randint(1,6)
print(f'Dice roll #1: {dice_roll_1}, Dice roll #2: {dice_roll_2}, Dice roll #3: {dice_roll_3}.')
total = dice_roll_1 + dice_roll_2 + dice_roll_3
print(f'The sum of the die rolls is: {total}.')