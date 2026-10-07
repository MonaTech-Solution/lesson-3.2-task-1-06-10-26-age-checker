# TASK NAME: Age Checker
"""
Goal: Write a tiny program that asks for an age and checks a comparison.
• Ask the user for age.
• Convert the input to an integer.
• Compare the age with 18.
• Print the result of the comparison.
• Use a meaningful variable name.
"""
age = int(input("How old are you?: "))
is_below_18 = age < 18 
print(f"{is_below_18}")
is_above_18 = age > 18
print(f"{is_above_18}")
is_atleast_18 = age >= 18
print(f"{is_atleast_18}")
is_atmost_18 = age <= 18
print(f"{is_atmost_18}")