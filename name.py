# Program to check whether a number is even or odd

def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"

# Input from user
try:
    num = int(input("Enter a number: "))
    result = check_even_odd(num)
    print(result)
except ValueError:
    print("Please enter a valid integer.")
