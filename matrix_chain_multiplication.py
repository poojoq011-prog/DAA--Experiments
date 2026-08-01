# Experiment No. 6
# Optimal Cost Computation in Matrix Chain Multiplication using Dynamic Programming

def matrix_chain_order(p):
    n = len(p) - 1

    # Cost table
    m = [[0 for _ in range(n)] for _ in range(n)]

    # Split table
    s = [[0 for _ in range(n)] for _ in range(n)]

    # Chain length
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')

            for k in range(i, j):
                cost = (
                    m[i][k]
                    + m[k + 1][j]
                    + p[i] * p[k + 1] * p[j + 1]
                )

                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s


def print_optimal_parenthesis(s, i, j):
    if i == j:
        return f"A{i + 1}"

    k = s[i][j]
    left = print_optimal_parenthesis(s, i, k)
    right = print_optimal_parenthesis(s, k + 1, j)

    return f"({left}{right})"


# Matrix dimensions
# A1 = 10x30
# A2 = 30x5
# A3 = 5x60
# A4 = 60x10
p = [10, 30, 5, 60, 10]

m, s = matrix_chain_order(p)

print("Matrix Dimensions:", p)
print("Minimum Scalar Multiplications:", m[0][len(p) - 2])
print("Optimal Parenthesization:", print_optimal_parenthesis(s, 0, len(p) - 2))

OUTPUT:
Matrix Dimensions: [10, 30, 5, 60, 10]
Minimum Scalar Multiplications: 5000
Optimal Parenthesization: ((A1A2)(A3A4))
