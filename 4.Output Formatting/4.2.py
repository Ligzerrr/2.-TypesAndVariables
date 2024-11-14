###
# Write a program that calculates and prints
# the income of a family per person. To print the results
# in a readable form, use f-strings.
#
father_income = 5450
mother_income = 4920
family_members = 5
total_income = mother_income + father_income #zarobki rodzicow lol
income_per_person = total_income / family_members #Nie wiem? Chyba powinno byc dzielone przez dwa bo tylko rodzice zarabiaja ale nie wiem
print(f'Total family income is {total_income}, and income per person is {income_per_person}.')