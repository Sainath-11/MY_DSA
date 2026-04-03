"""
General Matrix operations :
            1) addition and sub 
            2) mulitplication 
            3) transpose 

"""

"""
General Matrix operations :
            1) addition and sub 
            2) mulitplication 
            3) transpose 

"""


class Solution:

    def MatrixAddition(self, mat1, mat2):
        r1, c1 = len(mat1), len(mat1[0])
        r2, c2 = len(mat2), len(mat2[0])

        if r1 != r2 or c1 != c2:
            return "Not Possible"
        else:
            result=list()
            for i in range(r1):
                row = []
                for j in range(c1):
                    row.append(mat1[i][j] + mat2[i][j])
                result.append(row)

            return result

    def MatrixSubtraction(self, mat1, mat2):
        r1, c1 = len(mat1), len(mat1[0])
        r2, c2 = len(mat2), len(mat2[0])

        if r1 != r2 or c1 != c2:
            return "Not Possible"
        else:
            result=list()
            for i in range(r1):
                row = []
                for j in range(c1):
                    row.append(mat1[i][j] - mat2[i][j])
                result.append(row)

            return result

    def Transpose(self, mat):
        r, c = len(mat), len(mat[0])
        result = []

        for j in range(c):       
            row = []
            for i in range(r):    
                row.append(mat[i][j])
            result.append(row)

        return result

    def MatrixMat(self, mat1, mat2):
        r1, c1 = len(mat1), len(mat1[0])
        r2, c2 = len(mat2), len(mat2[0])

        if c1 != r2:
            return "Not Possible"

        result = [[0]*c2 for _ in range(r1)]

        for i in range(r1):
            for j in range(c2):
                for k in range(c1):
                    result[i][j] += mat1[i][k] * mat2[k][j]

        return result




def inputMatrix(name):
    r = int(input(f"Enter rows of {name}: "))
    c = int(input(f"Enter cols of {name}: "))

    print(f"Enter elements of {name} row-wise:")

    mat = []
    for i in range(r):
        row = list(map(int, input().split()))
        mat.append(row)

    return mat


def printMatrix(mat):
    if isinstance(mat, str):
        print(mat)
        return
    for row in mat:
        print(*row)
    print()




def main():
    obj = Solution()

    print("Choose operation:")
    print("1 → Addition")
    print("2 → Subtraction")
    print("3 → Multiplication")
    print("4 → Transpose")

    choice = int(input("Enter choice: "))

    if choice == 4:
        mat = inputMatrix("Matrix")
        result = obj.Transpose(mat)
        print("Result:")
        printMatrix(result)

    else:
        mat1 = inputMatrix("Matrix 1")
        mat2 = inputMatrix("Matrix 2")

        if choice == 1:
            result = obj.MatrixAddition(mat1, mat2)
        elif choice == 2:
            result = obj.MatrixSubtraction(mat1, mat2)
        elif choice == 3:
            result = obj.MatrixMat(mat1, mat2)
        else:
            print("Invalid choice")
            return

        print("Result:")
        printMatrix(result)


if __name__ == "__main__":
    main()
    
        



        