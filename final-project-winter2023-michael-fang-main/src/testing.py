import csv_reader


# test tuple matrix
matrix = (
    (1, 2, 3, 4),
    (5, 6, 7, 8),
    (9, 10, 11, 12),
    (13, 14, 15, 16)
)

column_matrix = ()
columns = ()
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        columns += (matrix[col][row], )
    column_matrix += (columns, )
    columns = ()

print(column_matrix)