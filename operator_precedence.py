'''
Operator Precedence Rules

PEMDAS

P - Parentheses
E - Exponents/Exponentiation
M/D - Multiplication/Division/Modulus (first come, first processed)
A/S - Addition/Subtraction (first come, first processed)

'''

result = 8 + 4 / 2 ** 3 - 1 * 6 % 3
# 1. Exponentiation: 2 ** 3 = 8
# 2. Division: 4 / 8 = 0.5
# 3. Multiplication: 1 * 6 = 6
# 4. Modulus: 6 % 3 = 0
# 5. Addition: 8 + 0.5 = 8.5
# 6. Subtraction: 8.5 - 0 = 8.5
print(result)

