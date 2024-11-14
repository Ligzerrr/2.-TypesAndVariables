###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input('a=') #bok a podstawy
b = input('b=') #bok b podstawy
c = input('c=') #wysokosc prostoslupa
a = int(a)
b = int(b)
c = int(c)
cuboid_volume = (a*b*c) #Pole podstawy * wysokosc
cuboid_surface_area = (a*b*2) + (a*c*2) + (b*c*2) #Powierzchnie wszystkich scian (trzy razy po dwa takie same prostokaty)
print(f'The volume of a cuboid with the sides a: {a}, b: {b}, c: {c} is equal to: {cuboid_volume} and the surface area of said cuboid is: {cuboid_surface_area}')