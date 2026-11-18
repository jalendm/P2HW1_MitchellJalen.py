# Jalen Mitchell
# November 18, 2026
# P2LAB1 - Circle Calculations
# This program asks the user for a circle's radius and calculates its
# diameter, circumference, and area.

# Pseudocode:
# 1. Ask the user to enter the circle's radius as a float.
# 2. Calculate the diameter by multiplying the radius by 2.
# 3. Calculate the circumference using 2 times pi times the radius.
# 4. Calculate the area using pi times the radius squared.
# 5. Display the results with the required decimal places.

import math

radius = float(input("Enter the radius of the circle: "))

diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print()
print("------------ Results ------------")
print(f"Radius:        {radius}")
print(f"Diameter:      {diameter:.1f}")
print(f"Circumference: {circumference:.2f}")
print(f"Area:          {area:.3f}")
