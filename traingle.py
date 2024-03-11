





def triangle_type(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle"
    elif a == b == c:
        return "Equilateral triangle"
    elif a == b or b == c or a == c:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"

# Manual Test Cases
manual_test_cases = [
    # Equilateral triangles
    (5, 5, 5),
    (10, 10, 10),
    # Isosceles triangles
    (5, 5, 8),
    (7, 5, 7),
    # Scalene triangles
    (3, 4, 5),
    (8, 6, 10),
    # Not a triangle
    (1, 1, 3),
    (0, 0, 0),  
]

# Test the triangle_type function with manual test cases
print("Manual Test Cases:")
for sides in manual_test_cases:
    a, b, c = sides
    print(f"Triangle with sides {a}, {b}, {c}:", triangle_type(a, b, c))
print()

# Generated Test Cases
generated_test_cases = [
    # Equilateral triangles
    (3, 3, 3),
    (4, 4, 4),
    (5, 5, 5),
    (6, 6, 6),
    (7, 7, 7),
    # Isosceles triangles
    (2, 2, 3),
    (3, 3, 4),
    (4, 4, 5),
    (5, 5, 6),
    (6, 6, 7),
    # Scalene triangles
    (2, 3, 4),
    (3, 4, 5),
    (4, 5, 6),
    (5, 6, 7),
    (6, 7, 8),
    # Not a triangle
    (1, 1, 5),
    (1, 5, 1),
    (5, 1, 1),
    (1, 2, 3),
    (2, 3, 1),
    (3, 1, 2),
    (0, 0, 1),
    (0, 1, 0),
    (1, 0, 0),
    (0, 0, 0),
    (10, 20, 30),
    (20, 30, 10),
    (30, 10, 20),
    (100, 200, 300),
    (200, 300, 100),
    (300, 100, 200),
    (500, 500, 1000),
    (500, 1000, 500),
    (1000, 500, 500),
    (1000, 1000, 2000),
    (1000, 2000, 1000),
    (2000, 1000, 1000),
    (5000, 5000, 10000),
    (5000, 10000, 5000),
    (10000, 5000, 5000),
    (10000, 10000, 20000),
    (10000, 20000, 10000),
    (20000, 10000, 10000),
    # Add more test cases here...
]

# Test the triangle_type function with generated test cases
print("Generated Test Cases:")
for sides in generated_test_cases:
    a, b, c = sides
    print(f"Triangle with sides {a}, {b}, {c}:", triangle_type(a, b, c))


