###
# A program that prints a university abbreviation
#   
university = "Krakow University of Economics"
abbreviation = "" #pusty string do ktorego zostanie przypisany skrot
for i in range(len(university)): #petla dla dlugosci calego wyrazenia
    if(university[i] == university[i].upper() and university[i] != ' '): abbreviation += university[i] #.upper to wielki znak if sprawdza czy znak jest wielki oraz czy nie jest spacja i dodaje kazda wielka litere do skrotu (pusty string abbreviation)
print(f'The abbreviation for: {university} is {abbreviation}')