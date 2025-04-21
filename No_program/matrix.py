from random import randint
n=6
matrix = [[randint(0, 9) for j in range(n)] for i in range(n)]
for row in matrix:
    print(*row)
print()
max_num_up = 0
max_num_low = 0
i_up, j_up = 0, 0
i_down, j_down = 0, 0
for i in range(n):
    for j in range(n):
        if (i<j and i< n-1-j) or (i<j and i>n-1-j):
            if matrix[i][j] > max_num_up:
                max_num_up = matrix[i][j]
                i_up, j_up = i, j

        if (i > j and i < n - 1 - j) or (i > j and i > n - 1 - j):
            if matrix[i][j] > max_num_low:
                max_num_low = matrix[i][j]
                i_down, j_down = i, j
matrix[i_up][j_up], matrix[i_down][j_down] = matrix[i_down][j_down], matrix[i_up][j_up]
for row in matrix:
    print(*row)