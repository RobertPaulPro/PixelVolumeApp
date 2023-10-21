import math

# Step 1: Get user input for the first two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2: Get user input for the third number
num3 = float(input("Enter the third number: "))

# Step 3: Perform the calculations
result = (num1 * num2)  # Multiply the first two numbers

if num1 != 0:
    result = result * math.sqrt(num3 / num1)  # Square root of (num3 / num1)

# Step 4: Display the final result
print("The result of the calculation is:", result)