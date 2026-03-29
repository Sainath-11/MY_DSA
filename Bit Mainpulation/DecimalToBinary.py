"""
Given a decimal number n, return its binary equivalent.
Examples :

Input: n = 12
Output: 1100
Explanation: The binary representation of 12 is "1100", since 12 = 1×2**3 + 1×2**2 + 0×2**1 + 0×2**0
Input: n = 33
Output: 100001
Explanation: The binary representation of 33 is "100001", since 33 = 1×2**5 + 0×2**4 + 0×2**3 + 0×2**2 + 0×2**1 + 1×2**0
Constraints:
1 ≤ n ≤ 2**31 - 1

"""

class Solution:
    def DecimalToBinary(self,num):
        bin=""
        while num >1:
            rem = num % 2
            num = num // 2
            bin = bin + str(rem)
        bin = bin + str(1)
        return bin[::-1]
    def DecimalToBinaryRec(self,num):
        if num ==1 :
            return str(1)
        bin = self.DecimalToBinaryRec(num//2)+str(num%2)
        return bin 
def main():
    num = int(input("enter the num:"))
    sol=Solution()
    print("iterative one: "+sol.DecimalToBinary(num))
    print("recursion one: "+sol.DecimalToBinaryRec(num))
if __name__ == "__main__":
    main()



    