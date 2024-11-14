###
# A program to calculate the volume and surface area of ​​a cube.
# 
cube_side_string = input('Enter cube side: ')
cube_side = int(cube_side_string)
cube_volume = cube_side**3 #Dlugosc boku/krawedzi do potegi 3 (wszystkie boki sa rowne)
cube_surface_area = cube_side**2 * 6 #Pole powierzchni calkowitej (6 scian * powierzchnia jednej sciany (kwadratu))
print(f'The volume of a cube with side {cube_side} is {cube_volume}')
print(f'The surface area of a cube with side {cube_side} is {cube_surface_area}')