def factorial(n):
    # Base case: if n is 0 or 1, factorial is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Input a number
num = int(input("Enter a non-negative integer: "))

# Check if the number is non-negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Calculate factorial using the factorial function
    result = factorial(num)
    print("Factorial of", num, "is", result)
