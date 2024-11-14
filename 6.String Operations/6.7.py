###
# A program that prints a numerical representation of each letter of your name.
#
name = 'Piotr' # replace John with your name
for i in range(len(name)): #Petla wykonywana (dlugosc imienia) razy 
    print(f'The letter {name[i]} has a code {ord(name[i])}')