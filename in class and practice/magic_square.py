def generate_4x4_magic_square():
    n = 4
    square = [[0 for _ in range(n)] for _ in range(n)]
    num = 1

    
    for i in range(n):
        for j in range(n):
            square[i][j] = num
            num += 1

   
    for i in range(n):
        for j in range(n):
            
            if (i == j) or (i + j == n - 1) or ((i == 0 or i == 3) and (j == 0 or j == 3)) or ((i == 1 or i == 2) and (j == 1 or j == 2)):
                continue
            else:
                square[i][j] = 17 - square[i][j]

    return square

# Print the magic square
magic_square = generate_4x4_magic_square()
print("4x4 Magic Square (each row/column/diagonal sums to 34):")
for row in magic_square:
    print(row)
