#original
'''age = input("What is your current age?")

days = int(age) * 365
weeks = int(age) * 52
months = int(age) * 12
current_age = 90 - age
time_left = current_age_days + current_age_weeks + current_age_months
time_left = (current_age_days + 'days, ') + current_age_weeks + 'weeks, ' + current_age_months + 'months')
print('You have ' + time_left)
'''
#refactored
age = input("What is your current age?")
age_as_int = int(age)
years_remaining = 90 - int(age) 
months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")