THRESHOLD_VALUE = 0.8

sample = "some data"
tokens = get_tokens(sample)

for i in range(0, len(tokens)):
    binary = get_binary(tokens[i])
    matrix = get_matrix(binary)
    corr = corr_calc(matrix)

    if corr >= THRESHOLD_VALUE:
        compress(matrix)

    # Return the compressed data
