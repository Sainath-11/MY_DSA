"""
Given an array, and an element num the task is to find if num is present in the given array or not. 
If present print the index of the element or print -1.
Example 1:
Input:
 arr[] = 1 2 3 4 5, num = 3  
Output:
 2  `
Explanation:
 3 is present at the 2nd index of the array.

Example 2:
Input:
 arr[] = 5 4 3 2 1, num = 5  
Output:
 0  
Explanation:
 5 is present at the 0th index of the array.

"""
class Solution:

    def linearSearch(self,arr,target)->int:
        for ele in range(len(arr)):
            if arr[ele]==target:
                return ele
        return -1
    
def main():
    n = int(input("Enter the size of array:"))
    l = list(map(int,input("enter the element of array:").split()))
    target =int(input("enter the target element:"))
    sol = Solution()
    print(sol.linearSearch(l,target))

if __name__ =="__main__":
    main()
