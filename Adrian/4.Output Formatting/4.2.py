###
# Write a program that calculates and prints
# the income of a family per person. To print the results
# in a readable form, use f-strings.
#
father_income = 5000
mother_income = 4400
family_members = 5
total_income = mother_income + father_income #zarobki rodzicow 
income_per_person = total_income / family_members 
print(f'Total family income is {total_income}, and income per person is {income_per_person}.')