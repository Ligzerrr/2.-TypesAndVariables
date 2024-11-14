# A program that reads your first and last name from the keyboard.
# Store this data in two separate variables.
# Then, print your full name i.e. first and last name separated by a single space.
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ') #Wczytywanie imienia i nazwiska
full_name =  first_name+ ' ' + last_name #Tak jak w c++ dodanie dwoch stringow pomiedzy nimi pusty znak (spacja) 
print(f'Your first name is {first_name} and your last name is {last_name}') #Wyswietlenie imienia i nazwiska
print(f'And your full name is {full_name}')