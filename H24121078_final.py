def parse_matrix(input_str):
    """
    Parse the input string to create a matrix (list of lists).
    """
    rows = input_str.split('|')
    matrix = [list(map(int, row.split(','))) for row in rows]
    return matrix

def matrix_multiply(U, V):
    """
    Multiply two matrices U and V.
    """
    n = len(U)
    # Initialize the result matrix M with zeros
    M = [[0] * n for _ in range(n)]
    
    # Perform matrix multiplication
    for i in range(n):
        for j in range(n):
            for k in range(n):
                M[i][j] += U[i][k] * V[k][j]
    
    return M

def print_matrix(matrix):
    """
    Print the matrix in the required format.
    """
    for row in matrix:
        print(row)

def main():
    # User inputs
    u_input = input("Enter matrix U: ")
    v_input = input("Enter matrix V: ")
    
    # Parse the inputs to create matrices
    U = parse_matrix(u_input)
    V = parse_matrix(v_input)
    
    # Store matrices in dictionaries
    matrices = {'U': U, 'V': V}
    
    # Multiply matrices U and V to get M
    M = matrix_multiply(matrices['U'], matrices['V'])
    
    # Output the result
    print("M = U x V")
    print_matrix(M)

if __name__ == "__main__":
    main()
