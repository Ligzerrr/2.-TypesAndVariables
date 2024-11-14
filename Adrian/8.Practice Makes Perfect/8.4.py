###
# A program that prints your height both in cm and in feet and inches.
#
cm = 174
feet = int(cm / 30.48) #1 foot = 30.48cm
inches = int((cm / 2.54) % 12) #1 inch = 2.54 cm 12 inch = 1 foot
# calculate the number of feet

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')