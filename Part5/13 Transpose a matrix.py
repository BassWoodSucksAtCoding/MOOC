# Write your solution here
def transpose(matrix: list):
    new_list_local = []
    for row in matrix:
        new_list_local.append(row[:])

    for row in range(len(matrix)):
        for column in range(len(matrix)):
            matrix[row][column] = new_list_local[column][row]
