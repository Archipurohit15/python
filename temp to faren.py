def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

# Input temperature in Fahrenheit
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

# Convert Fahrenheit to Celsius
celsius = fahrenheit_to_celsius(fahrenheit)

# Output the result
print("Temperature in Celsius:", celsius)
