"""
Given an array arr[] of size n, find the element that appears more than ⌊n/2⌋ times. 
If no such element exists, return -1.

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
The input is generated such that a majority element will exist in the array.
"""

class Solution:
    #brute force --> hashmap if element count is greater than floor(n/2) then answer or else -1 
    def burteforce(self,arr):
        d={}
        for i in range(len(arr)):
            if arr[i] in d :
                d[arr[i]] = d[arr[i]]+1
            else:
                d[arr[i]] =1
        n = len(arr)

        for value,items in d.items():
            if d[value] > n//2 :
                return value
        return -1
    def MooresVotingAlgo(self,arr):
        ele = 0 
        count= 0 
        for i in range(len(arr)):
            if count == 0 :
                ele = arr[i]
                count = count + 1
            elif ele == arr[i]:
                count = count + 1
            else:
                count = count -1 
        count1=0
        for i in range(len(arr)):
            if arr[i] == ele :
                count1 = count1+1
        if count1 > len(arr)//2:
            return ele 
        return -1
    
def main():
    n = int(input("Enter the size of array:"))
    l = list(map(int,input("Enter the size of array:").split()))
    sol = Solution()
    print(sol.burteforce(l))
    print(sol.MooresVotingAlgo(l))

if __name__ == "__main__":
    main()

        
