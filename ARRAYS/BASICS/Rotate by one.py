
"""

Problem Statement: Given an integer array nums, rotate the array to the left by one.

Note: There is no need to return anything, just modify the given array.

Example 1:
Input:
 nums = [1, 2, 3, 4, 5]  
Output:
 [2, 3, 4, 5, 1]  
Explanation:
 Initially, nums = [1, 2, 3, 4, 5]  
Rotating once to the left results in nums = [2, 3, 4, 5, 1].

Example 2:
Input:
 nums = [-1, 0, 3, 6]  
Output:
 [0, 3, 6, -1]  
Explanation:
 Initially, nums = [-1, 0, 3, 6]  
Rotating once to the left results in nums = [0, 3, 6, -1].


"""

class Solution:
    def rotatedbyOne(self,arr):
        temp =arr[0]
        for i in range(1,len(arr)):
            arr[i-1]=arr[i]
        arr[len(arr)-1]=temp 

def main():
    n = int(input("enter the size of array:"))
    l = list(map(int,input("enter the elements of array :").split()))
    sol = Solution()
    sol.rotatedbyOne(l)
    print(l)

if __name__ == "__main__":
    main()
        
