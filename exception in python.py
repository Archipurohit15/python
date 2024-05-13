# Define a custom exception class
class CustomException(Exception):
    def __init__(self, message="This is a custom exception"):
        self.message = message
        super().__init__(self.message)

# Function to raise the custom exception
def check_number(num):
    if num < 0:
        raise CustomException("Number should be greater than or equal to 0")
    else:
        print("Number is valid")

# Main program
try:
    # Get user input
    num = int(input("Enter a number: "))
    
    # Check if the number is valid
    check_number(num)
    
except CustomException as ce:
    print("Custom Exception:", ce)

except ValueError:
    print("Please enter a valid integer.")

except Exception as e:
    print("An error occurred:", e)
