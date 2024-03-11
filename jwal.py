

def triangle_type(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle"
    elif a == b == c:
        return "Equilateral triangle"
    elif a == b or b == c or a == c:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"

# Example usage:
# a = float(input("Enter the length of side a: "))
# b = float(input("Enter the length of side b: "))
# c = float(input("Enter the length of side c: "))

# print("Type of triangle:", triangle_type(a, b, c))

# Generate test cases
import random
test_cases = []
for _ in range(10):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    test_cases.append((a, b, c))
print("Generated Test Cases:")
for sides in test_cases:
    a, b, c = sides
    print(f"Triangle with sides {a}, {b}, {c}:", triangle_type(a, b, c))

# Manual Test Cases
manual_test_cases = [
    (3, 4, 5),  # Right-angled triangle
    (5, 5, 8),  # Isosceles triangle
    (7, 7, 7),  # Equilateral triangle
    (2, 3, 6)   # Not a triangle
]
print("Manual Test Cases:")
for sides in manual_test_cases:
    a, b, c = sides
    print(f"Triangle with sides {a}, {b}, {c}:", triangle_type(a, b, c))
