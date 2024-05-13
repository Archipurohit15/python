class PowerCalculator:
    def calculate_power(self, x, n):
        result = 1
        
        # Handle negative exponent
        if n < 0:
            x = 1 / x
            n = -n
        
        # Calculate power using repeated squaring algorithm
        while n:
            if n % 2:
                result *= x
            x *= x
            n //= 2
        
        return result

# Example usage
power_calculator = PowerCalculator()
x = float(input("Enter the base (x): "))
n = int(input("Enter the exponent (n): "))
result = power_calculator.calculate_power(x, n)
print("Result:", result)
