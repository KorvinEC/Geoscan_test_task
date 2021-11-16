import matplotlib.pyplot as plt


def main(input_array):
    print(f'input_array: {input_array}')

    x_min, x_max = min(input_array[0]), max(input_array[0])

    print(f'min and max: {x_min}, {x_max}')

    sym = (x_min + x_max) / 2

    print(f'sym        : {sym}')

    left_side = [i for i, val in enumerate(input_array[0]) if val < sym]
    right_side = [i for i, val in enumerate(input_array[0]) if val > sym]

    if len(left_side) != len(right_side):
        return None

    res = {}

    for i in left_side:
        if input_array[1][i] not in res.keys():
            res[input_array[1][i]] = [input_array[0][i]]
        else:
            res[input_array[1][i]].append(input_array[0][i])

    print(f'left       : {res}')

    for i in right_side:
        if input_array[1][i] not in res.keys():
            print('No such element')
            return None
        else:
            if not any([abs(input_array[0][i] - sym) == abs(j - sym) for j in res[input_array[1][i]]]):
                return None

    plt.scatter(input_array[0], input_array[1])
    plt.axvline(x=sym)
    plt.show()

    return sym


if __name__ == '__main__':
    test_data = [
        [[0, 1, 2, 3], [1, 2, 2, 1]],
        [[0, 1, 2, 3], [1, 2, 3, 4]],
        [[0, -1, -2, -3], [1, 2, 2, 1]],
        [[3, 2, 1, 0], [1, 2, 2, 1]],
        [[-3, -2, -1, 0], [1, 2, 2, 1]],
    ]

    for test in test_data:
        res = main(test)
        print(res)
