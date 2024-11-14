###
# A program that checks if a tree can be cut down
c = [160, 90, 230, 120] #prosta lista zawierajaca wszystkie wartosci podane w cwiczeniu
for i in range(4): #petla wykonywana 4 razy (dla kazdego drzewa)
    diameter = c[i] / 3.14 #diameter == srednica czyli promien pomnozony przez 2 ktory obliczamy z obwodu koła
    print(f'The diameter of tree: {i} is equal to: {round(diameter)}.') 
    print(f'The tree can be cut down: {diameter > 50}') #bool sprawdzajacy czy srednica jest wieksza rowna 50 cm
