import fibonacci

# Input number of Fibonacci numbers to generate
n = int(input("Enter the number of Fibonacci numbers to generate: "))

# Call the fibonacci function from the Fibonacci module
fib_numbers = fibonacci.fibonacci(n)

# Print the generated Fibonacci numbers
print("Fibonacci sequence up to the", n, "th Fibonacci number:", fib_numbers)
