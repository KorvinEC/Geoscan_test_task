import math

input_array = [[2, 3, 4, 5, 6], [2, 1, 0, 1, 2]]

print(f'input_array: {input_array}')

x_min, x_max = min(input_array[0]), max(input_array[0])

print(f'min and max: {x_min}, {x_max}')

sym = (x_min + x_max) / 2

res = {input_array[1][i]: x for i, x in enumerate(input_array[0]) if x < sym}

print(f'First half: {res}')

result = sym

for i, x in enumerate(input_array[0]):
    if x > sym:
        if input_array[1][i] in res.keys():
            print(True)
        else:
            result = None
            print(False)

print(result)


