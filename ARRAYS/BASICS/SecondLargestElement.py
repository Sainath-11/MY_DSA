"""
Given an array of integers nums, return the second-largest element in the array. 
If the second-largest element does not exist, return -1.

Example 1
Input: nums = [8, 8, 7, 6, 5]
Output: 7
Explanation:
The largest value in nums is 8, the second largest is 7

Example 2
Input: nums = [10, 10, 10, 10, 10]
Output: -inf
Explanation:
The only value in nums is 10, so there is no second largest value, thus -1 is returned

Constraints:
1 <= nums.length <= 10**5
-10**4 <= nums[i] <= 10**4
nums may contain duplicate elements.

"""

class Solution:
    def secondLargestElement(self,arr)->int :
        largeele = float('-inf')
        secondele = float('-inf')

        for ele in range(len(arr)):
            if arr[ele] > largeele :
                secondele = largeele 
                largeele = arr[ele]
            elif arr[ele] < largeele  and arr[ele] > secondele:
                secondele = arr[ele]
        return secondele 
    
def main():
    n = int(input("enter the size of arrya:"))
    l=list(map(int, input("enter the element of array:").split()))
    sol = Solution()
    result = sol.secondLargestElement(l)
    print(result)

if __name__ == "__main__":
    main()

