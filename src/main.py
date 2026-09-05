import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import square, is_even, celsius_to_fahrenheit

def main():
    try:
        user_input = float(input("Enter a number: "))
        num = int(user_input) if user_input.is_integer() else user_input
        
        print(f"Square: {square(num)}")
        print(f"Even: {is_even(num)}")
        print(f"Fahrenheit: {celsius_to_fahrenheit(num)}°F")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
