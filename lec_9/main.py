class Matrix:
    def __init__(self, rows, columns, data=None):
        self.rows = rows
        self.columns = columns
        if data is None:
            self.data = [[0 for _ in range(columns)] for _ in range(rows)]
        else:
            if len(data) != rows or any(len(row) != columns for row in data):
                raise ValueError("Provided data dimensions do not match the specified rows and columns.")
            self.data = data

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.data])

    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrix dimensions must match for addition.")
        result_data = [[self.data[i][j] + other.data[i][j] for j in range(self.columns)] for i in range(self.rows)]
        return Matrix(self.rows, self.columns, result_data)

    def __sub__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Matrix dimensions must match for subtraction.")
        result_data = [[self.data[i][j] - other.data[i][j] for j in range(self.columns)] for i in range(self.rows)]
        return Matrix(self.rows, self.columns, result_data)

    def __mul__(self, other):
        if self.columns != other.rows:
            raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix for multiplication.")
        result_data = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.columns)) for j in range(other.columns)] for i in range(self.rows)]
        return Matrix(self.rows, other.columns, result_data)

matrix1 = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
matrix2 = Matrix(3, 2, [[7, 8], [9, 10], [11, 12]])

print("Matrix 1:")
print(matrix1)

print("Matrix 2:")
print(matrix2)

result_multiplication = matrix1 * matrix2
print("Matrix 1 * Matrix 2:")
print(result_multiplication)

matrix1 = Matrix(3, 2, [[7, 8], [9, 10], [11, 12]])
matrix2 = Matrix(3, 2, [[7, 8], [9, 10], [11, 12]]) 

result_addition = matrix1 + matrix2
print("Matrix 1 + Matrix 2:")
print(result_addition)

result_subtraction = matrix1 - matrix2
print("Matrix 1 - Matrix 2:")
print(result_subtraction)

