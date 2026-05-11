import numpy as np

def create_234_array():
    data = [
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],
        [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
    ]
    
    return np.array(data)

my_array = create_234_array()
print("Array Shape:", my_array.shape)
print("The Array:\n", my_array)