"""
Given a string b representing a Binary Number, The problem is to find its decimal equivalent.
Examples:

Input : b = 111
Output : 7
Explanation : The decimal equivalent of the binary number 111 is 22 + 21 + 20 = 7.
Input : b = 1010
Output : 10
Explanation : The decimal equivalent of the binary number 1010 is 23 + 21 = 10.
Input: b = 100001
Output: 33
Explanation : The decimal equivalent of the binary number 100001 is 25 + 20 = 33.



"""

class Solution:
	def binaryToDecimal(self, b)->int:
		n = len(b)
		ans= 0
		for i in range(n):
			if b[i] =="1":
				ans = ans + (1<<(n-i-1))
		return ans
	

def main():
	binary = input("Enter the binary string:")
	sol = Solution()
	print(sol.binaryToDecimal(binary))
	
if __name__ == "__main__":
	main()
	
	