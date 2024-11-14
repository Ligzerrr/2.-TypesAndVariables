import random #importuje biblioteke random
print("Dice rolling simulator") #wyswietla napis
for i in range(5): #petla powtarzajaca sie 5 razy
    dice_roll = random.randint(1,6) #losowanie liczby 
    print(dice_roll, end=" ") #wyswieltanie wylosowanej liczby