import numpy as np
from my_python_package.operators import add, multiply
def main():
    print("add(1, 3):", add(1, 3))
    print("multiply(2, 12.):", multiply(2, 12.0))
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = 2.0 * np.ones(A.shape)
    print("A:\n", A)
    print("B:\n", B)
    print("add(A, B):\n", add(A, B))
    print("multiply(A, B):\n", multiply(A, B))
if __name__ == "__main__":
    main()
