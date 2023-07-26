def calculate_age(birth_year, current_year):
    age = current_year - birth_year
    return age

# Get the birth year from the user
birth_year = int(input("Enter your birth year: "))

# Get the current year (you can also use a library like datetime to get the current year programmatically)
current_year = int(input("Enter the current year: "))

# Calculate the age and display it
age = calculate_age(birth_year, current_year)
print(f"You are {age} years old.")
