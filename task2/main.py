import numpy as np

def gauss_jordan(A, b):
    augmented_matrix = np.hstack((A, b.reshape(-1, 1)))
    reduced_row_echelon_form, pivot_columns = np.linalg.qr(augmented_matrix, mode='complete')
    solution = reduced_row_echelon_form[:, -1]
    return solution

def gauss_elimination(A, b):
    augmented_matrix = np.hstack((A, b.reshape(-1, 1)))
    row_echelon_form, pivot_columns = np.linalg.qr(augmented_matrix, mode='complete')
    solution, residuals, rank, singular_values = np.linalg.lstsq(row_echelon_form[:, :-1], row_echelon_form[:, -1], rcond=None)
    return solution

def jacobi_method(A, b, initial_guess, max_iterations=100, tolerance=1e-6):
    D = np.diag(np.diag(A))
    LU = A - D
    x = initial_guess
    for iteration in range(max_iterations):
        x_new = np.linalg.solve(D, b - np.dot(LU, x))
        if np.linalg.norm(x_new - x) < tolerance:
            return x_new
        x = x_new
    return x

def gauss_seidel_method(A, b, initial_guess, max_iterations=100, tolerance=1e-6):
    L = np.tril(A, k=-1)
    U = A - L
    x = initial_guess
    for iteration in range(max_iterations):
        try:
            x_new = np.linalg.solve(L, b - np.dot(U, x))
        except np.linalg.LinAlgError as e:
            print("Error:", e)
            return None  # Return None or handle the error as needed
        if np.linalg.norm(x_new - x) < tolerance:
            return x_new
        x = x_new
    print("Gauss-Seidel method did not converge.")
    return None

# Define the matrices and vectors for each system of equations
A1 = np.array([[2, 5, 7], [2, 1, -1], [1, 1, 1]])
b1 = np.array([52, 0, 9])

A2 = np.array([[2, 1, 5, 1], [1, 1, -3, 4]])
b2 = np.array([5, -1])

A3 = np.array([[1, 1, 1], [2, -3, 4], [3, 4, 5]])
b3 = np.array([9, 13, 40])

A4 = np.array([[5, -1, 1], [2, 4, 0], [1, 1, 5]])
b4 = np.array([10, 12, -1])

# Solve systems using different methods
solution_gauss_jordan = gauss_jordan(A1, b1)
solution_gauss_elimination = gauss_elimination(A2, b2)
solution_jacobi = jacobi_method(A3, b3, np.array([2, 3, 0]))
solution_gauss_seidel = gauss_seidel_method(A4, b4, np.array([0, 0, 0]))

# Print the solutions
print("Gauss-Jordan Method Solution:", solution_gauss_jordan)
print("Gauss Elimination Method Solution:", solution_gauss_elimination)
print("Jacobi Method Solution:", solution_jacobi)
print("Gauss-Seidel Method Solution:", solution_gauss_seidel)
