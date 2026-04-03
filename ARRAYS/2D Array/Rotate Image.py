"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
 DO NOT allocate another 2D matrix and do the rotation.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""

class Solution:
    def revrse(self,arr,low,high):
        if low >high:
            return 
        arr[low],arr[high]=arr[high],arr[low]
        self.revrse(arr,low+1,high-1)
    
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        print(matrix[0])
        for row in range(len(matrix)):
            for col in range(row+1,len(matrix[row])):
                matrix[row][col],matrix[col][row] = matrix[col][row],matrix[row][col]
        for row in range(len(matrix)):
                self.revrse(matrix[row],0,len(matrix[row])-1)

def main():
    n = int(input("Enter the size of matrix"))
    l =list()
    for row in range(n):
        row = list()
        for j in range(n):
            row.append(int(input()))
        l.append(row)
    sol = Solution()
    sol.revrse(l)

if __name__ =="__main__":
    main()
    
    
        
