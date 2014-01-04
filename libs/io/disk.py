

def matrix_to_csv(path, input_iter):
    with open(path, 'w') as storage:
        for row in input_iter:
            storage.write(','.join(map(str, row)) + '\n')
            yield row