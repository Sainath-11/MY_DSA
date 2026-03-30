
"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


"""

class Solution:
    def reverse(self,arr,low,high):
        if low>=high:
            return 
        arr[low],arr[high]=arr[high],arr[low]
        self.reverse(arr,low+1,high-1)
    
    def apporachOne(self,arr,k):
        # create a other array and store elements TC:o(n) SC:O(N)
        if k==0 :
            return arr
        else:
            n = len(arr)
            b=[0]*n
            while k>=n:
                k = k % n
            for i in range(k):
                b[i]= arr[n-k+i]
            for i in range(k,n):
                b[i] = arr[i-k]
        return b
    def apporachTwo(self,arr,k):
        # in place swaping TC:O(N) SC:O(1)
        """
            reverse entire array 
            reverse 0 to k-1 
            reverse k to n
        """
        n=len(arr)
        self.reverse(arr,0,n-1)
        self.reverse(arr,0,k-1)
        self.reverse(arr,k,n-1)
        return arr


    
def main():
    n = int(input("Enter the size of array:"))
    l= list(map(int,input("Enter the element of array:").split()))
    k = int(input("enter the value of k:"))
    sol = Solution()
    print(sol.apporachTwo(l,k))

if __name__ == "__main__":
    main()


         
        
