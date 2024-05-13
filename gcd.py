import math

# Input two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Find gcd using math.gcd()
gcd = math.gcd(num1, num2)

print("GCD of", num1, "and", num2, "is", gcd)
