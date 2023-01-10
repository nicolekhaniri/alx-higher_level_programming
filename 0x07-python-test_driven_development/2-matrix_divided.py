def matrix_divided(matrix, div):
    new_matrix = []
    list_len = len(matrix[0])
    
    if type(matrix) is not list:
        raise TypeError ("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if len(matrix[0])  
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int or type(div) is not float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError(" division by zero")
    else:
        matrix / div
        
    return
