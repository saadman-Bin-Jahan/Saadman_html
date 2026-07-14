import math

def calculate_circumference(radius):
    """Calculates the circumference of a circle given its radius."""
    return 2 * math.pi * radius

# Example usage:
radius = 5
circumference = calculate_circumference(radius)
print(f"The circumference of a circle with radius {radius} is {circumference:.2f}")
