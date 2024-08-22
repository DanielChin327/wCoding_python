# How to use argparse

# argparse is a standard library that allows you to easily write user friendly command-line interfaces


# Step 1: Import the module
import argparse

# Step 2: Creat and ArgumentParser Object
parser = argparse.ArgumentParser(description = "give a temp to convert to C")

# Step 3: Define Various Command-Line Arguments
parser.add_argument('fahrenheit', type=float, help="temp is fahrenheit")


# Step 4: Parse the Arguments
args = parser.parse_args()


def fahrenheit_to_celsius(temp):
    return (temp - 32) * (5.0/9.0)


celsius = fahrenheit_to_celsius(args.fahrenheit)

print(f"{args.fahrenheit}°F is equal to {celsius:.2f}°C")
