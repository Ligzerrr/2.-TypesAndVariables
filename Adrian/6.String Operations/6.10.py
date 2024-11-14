###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print(f'{movie.upper()}') #duze litery

# print title in small letters
print(f'{movie.lower()}') #male litery

# print how many times the vowel "e" appears in the title
print(f'{movie.count("e")}') #zwraca ilosc razy wystepowania litery "e" w tekscie

# print where in the text is the word "Lord"
print(f'{movie.find("Lord")}') #zwraca pozycje na ktorej znajduje sie slowo

# print where in the text is the word "dragon"
print(f'{movie.find("dragon")}') #Zwraca -1 poniewaz nie ma slowa dragon w tekscie