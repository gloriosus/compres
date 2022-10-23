import math
import numpy as np

SET_SIZE = 8


def get_sets(data: str, size: int):
    sets = []
    count = math.ceil(len(data) / size)
    for i in range(0, count):
        sets.append(data[i * size:(i + 1) * size])
    return sets


def get_binary(set: str):
    return "".join(f"{ord(x):08b}" for x in set)


def get_matrix(binary: str):
    matrix = np.array(list(binary), dtype=int)
    return np.reshape(matrix, (-1, optimal_size(len(matrix))[1]))


def optimal_size(length: int):
    row = 1
    col = length
    while row < col:
        if (row * 2) > (col / 2):
            break
        col = col / 2
        row = row * 2
    return row, int(col)


def get_blocks(matrix: np.ndarray) -> list:
    num_rows, num_cols = matrix.shape
    max_rows = int(num_rows / 4)
    max_cols = int(num_cols / 4)

    blocks = list()

    for i_row in range(0, max_rows):
        for i_col in range(0, max_cols):
            if i_row != 0 or i_col != 0:
                blocks.append(matrix[0:i_row+1, 0:i_col+1])

    return blocks


sample = "helloworldstring"
result_sets = get_sets(sample, SET_SIZE)

# Step 1
word = get_binary(result_sets[0])
# Step 2
matrix = get_matrix(word)
# Step 3
blocks = get_blocks(matrix)

print(word)
print(get_matrix(word))

print(blocks[2])
