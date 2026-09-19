
#Q-5: filter() and map() with Lambda
salaries = [3000, 4500, 6000, 2500, 7000]

# Get salaries less than 5000
low_earning = list(filter(lambda x: x < 5000, salaries))

# Give 10% bonus
bonus_salaries = list(map(lambda x: x * 1.10, low_earning))

print("Original salaries:", salaries)
print("Salaries less than 5000:", low_earning)
print("After 10% bonus:", bonus_salaries)