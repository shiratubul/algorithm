import numpy as np

def create_matrix():
    matrix = np.array([
        [ 1,  2,  3,  4,  5,  6],
        [ 7,  8,  9, 10, 11, 12],
        [13, 14, 15, 16, 17, 18],
    ], dtype=float)
    return matrix


def main():
    matrix = create_matrix()
    print(matrix.ndim)
    print(matrix.shape)
    print(matrix.dtype)


if __name__ == '__main__':
    main()