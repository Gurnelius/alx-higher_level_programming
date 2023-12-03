#!usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        size = len(i)
        for j in i:
            if j != i[size-1]:
                print(j, end=" ")
            else:
                print(j, end='')
        print('$')
