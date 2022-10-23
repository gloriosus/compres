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


def get_blocks(matrix: np.ndarray, size: tuple) -> list:
    blocks = list()

    for i_row in range(0, int(matrix.shape[0] / size[0])):
        for i_col in range(0, int(matrix.shape[1] / size[1])):
            blocks.append(matrix[i_row*size[0]:i_row*size[0]+size[0], i_col*size[1]:i_col*size[1]+size[1]])

    return blocks


def get_overlaps(block: np.ndarray) -> list:
    overlaps = list()
    flat = block.flatten()

    for i in range(0, len(flat)):
        count = 0
        for j in range(0, len(flat)):
            if flat[i] == flat[j]:
                count = count + 1
        overlaps.append(count)

    return overlaps


sample = "helloworldstring"
result_sets = get_sets(sample, SET_SIZE)

# Step 1
word = get_binary(result_sets[0])
# Step 2
matrix = get_matrix(word)
# Step 3
blocks = get_blocks(matrix, (2, 2))
# Step 4
overlaps = get_overlaps(blocks[3])

print(word)
print(get_matrix(word))

print(overlaps)
