""""

560. Subarray Sum Equals K
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107


"""

class Solution:
    def burteforce(self,nums,target):
        # generate all subarrays and check is subarray sum equal to sum k 
        # TC : O(N**3)
        count = 0 
        n = len(nums)
        for i in range(n):
            for j in range(i,n):
                total = 0 
                for k in range(i,j+1):
                    total = total + nums[k]
                if total == target :
                    count= count + 1
        return count
    
    def carryforward(self,nums,target):
        # carrat forward the older sum rather than recomupting again from scrtach 
        # TC : O(N**2)
        count = 0 
        n = len(nums)
        for  i in range(n):
            total = 0
            for j in range(i,n):
                total = total + nums[j]
                if total == target :
                    count = count + 1
        return count
    
    def prefixsumHashmap(self,nums,target):
        # prefix sum . find pf-target in hashmap and aslo add d[req] not 1 
        # TC:0(N) SC:0(N)
        d={}
        d[0]=1
        count = 0 
        pf=0
        for i in range(len(nums)):
            pf = pf + nums[i]
            req = pf - target 
            if req in d :
                count = count + d[req]
            d[pf]=d.get(pf,0)+1
        return count 
                
def main():
    n = int(input("Enter the size of array:"))
    l = list(map(int,input("Enter the elements of array:").split()))
    target = int(input("Enter the target:"))
    sol = Solution()
    print(sol.prefixsumHashmap(l,target))

if __name__ =="__main__":
    main()


        