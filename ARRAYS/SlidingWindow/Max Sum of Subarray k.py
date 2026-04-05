"""

Given an array of integers arr[]  and a number k. Return the maximum sum of a subarray of size k.

Note: A subarray is a contiguous part of any given array.

Examples:

Input: arr[] = [100, 200, 300, 400], k = 2
Output: 700
Explanation: arr2 + arr3 = 700, which is maximum.
Input: arr[] = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4
Output: 39
Explanation: arr1 + arr2 + arr3 + arr4 = 39, which is maximum.
Input: arr[] = [100, 200, 300, 400], k = 1
Output: 400
Explanation: arr3 = 400, which is maximum.
Constraints:
1 ≤ arr.size() ≤ 10**6
0 ≤ arr[i] ≤ 10**6
1 ≤ k ≤ arr.size()


"""

class Solution:
    def bruteforce(self,arr,k): #TC:O(N**2)
        n = len(arr)
        ans=0
        for i in range(n-k+1):
            sumw = 0
            for j in range(k):
                sumw = sumw + arr[i+j]
            ans = max(ans,sumw)
        return ans
    
    def slidingwindow(self,arr,k): #TC:O(N)
        #cacluate the window size ans first
        ans = 0
        for i in range(k):
            ans = ans + arr[i]
        # print(ans)
        
        # slindign windiw two pointer low,high, expand high++, shrink low--
        n=len(arr)
        low = 0 
        temp = ans
        for high in range(k,n):
            ans = ans + arr[high]-arr[low]
            low = low + 1
            temp = max(temp,ans)
        return temp
            


def main():
    n = int(input("Enter the size of array:"))
    k = int(input("Enter the size of window:"))
    l = int(map(int ,input("Enter the element of arrays:").split()))
    sol = Solution()
    print(sol.slidingwindow(l,k))

if __name__ =="__main__":
    main()
    