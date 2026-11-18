# Jalen Mitchell
# November 18, 2026
# P2LAB2 - Automobile MPG
# This program calculates how many gallons of gas a vehicle needs.

# Pseudocode:
# Create a dictionary of vehicles and their MPG.
# Display the vehicle keys.
# Ask the user to enter a vehicle.
# Display the vehicle's MPG.
# Ask how many miles they will drive.
# Calculate and display the gallons of gas needed.

# Create dictionary
cars = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Get dictionary keys
keys = cars.keys()

# Display keys
print(keys)

# Ask user for vehicle
vehicle = input("\nEnter a vehicle to see its MPG: ")

# Display MPG
mpg = cars[vehicle]
print(f"\nThe {vehicle} gets {mpg} MPG.")

# Ask for miles
miles = float(input(f"How many miles will you drive the {vehicle}? "))

# Calculate gallons needed
gallons = miles / mpg

# Display result
print(f"\nThe {gallons:.2f} gallons of gas are needed to drive the {vehicle} {miles} miles.")
