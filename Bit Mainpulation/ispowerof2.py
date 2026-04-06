"""

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.


Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false

"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        c= 0
        if n < 0:
            return False
        while n!=0 :
            n = n & (n-1)
            c= c + 1
        if c!=1:
            return False
        return True
        
def main():
    n = int(input("Enter the number:"))
    sol = Solution()
    print(sol.isPowerOfTwo(n))


if __name__ =="__main__":
    main()
