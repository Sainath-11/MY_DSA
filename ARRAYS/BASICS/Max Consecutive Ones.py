"""
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""

class Solution:
    #tc:o(n) sc:o(1)
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        ans = 0
        c= 0
        for  i in range(len(nums)):
            if nums[i]==0:
                c = 0
            else:
                c=c+1
            ans = max(ans,c)
        return ans
    
def main():
    n =int(input("Enter the size of array:"))
    l = list(map(int, input().split()))
    sol = Solution()
    sol.findMaxConsecutiveOnes(l)

if __name__ =="__main__":
    main()
