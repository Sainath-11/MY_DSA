"""

Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.


Example 1

Input: nums = [10, 5, 2, 7, 1, 9],  k=15

Output: 4

Explanation:

The longest sub-array with a sum equal to 15 is [5, 2, 7, 1], which has a length of 4. 
This sub-array starts at index 1 and ends at index 4, and the sum of its elements (5 + 2 + 7 + 1) equals 15. 
Therefore, the length of this sub-array is 4.

Example 2

Input: nums = [-3, 2, 1], k=6

Output: 0

Explanation:

There is no sub-array in the array that sums to 6. Therefore, the output is 0.

Constraints

 1<=n<=10**5
 -10**5<=nums[i]<=10**5
 -10**9<= k<=10**9

"""
class Solution:
    def bruteforce(self,nums,target):
        ans=-1
        n = len(nums)
        for i in range(n):
            for j in range(i,n):
                sumx = 0
                for k in range(i,j+1):
                    sumx = sumx + nums[k]
                if sumx == target:
                    ans = max(ans,j-i+1)
        return ans
    
    def carryForward(self,nums,target):
        n = len(nums)
        ans=-1
        for i in range(n):
            sumx=nums[i]
            for j in range(i+1,n):
                sumx = sumx + nums[j]

                if sumx == target:
                    ans = max(ans,j-i+1)
        return ans
    
    def HashMapApporach(self,nums,target):
        d={}
        ans = 0
        pf = 0
        for i in range(len(nums)):
            pf = pf +nums[i]
            if pf == target :
                ans = max(ans ,i+1)
            req = pf - target
            if req in d:
                ans = max(ans , i-d[req])
            d[pf]=i
        return ans
    def sldingwindowApporach(self,nums,target):
        low ,high = 0 ,0 
        n = len(nums)
        res = float('-inf')
        sumx =0 
        while high < n :
            sumx = sumx + nums[high] 
            while sumx > target  and low <=high :
                sumx = sumx - nums[low]
                low = low + 1
            if sumx == target :
                res = max(res,high-low+1)
            high = high + 1
        return res







                     

    # def longestSubarray(self, nums, k):

def main():
    n = int(input("Enter the size of array:"))
    l = list(map(int,input("Enter the elements of array:").split()))
    k = int(input("Enter the target:"))

    sol = Solution()
    print(sol.bruteforce(l,k))
    print(sol.carryForward(l,k))
    print(sol.HashMapApporach(l,k))
    print(sol.sldingwindowApporach(l,k))


if __name__ =="__main__":
    main()

