###
# Printing student's personal data
#
name = "Adrian"
age = input('Your age: ') #pobieranie wieku
age = int(age) #konwersja na inta poniewaz wszystko wczytane przez input jest traktowane jako string!
height = input('Your height in cms: ') #pobieranie wzrostu 
print(f"My name is {name}.")
print(f"I am {age} years old, and my height is {height} cm.")
print(f"In 6 years I will be {age+6} years old.") 