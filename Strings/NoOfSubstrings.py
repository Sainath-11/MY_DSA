"""
Genrate the number of substrings
str ="abcd"

subarrays: o((n*(n+1))//2)
   a             b         c          d
   a,b           b,c      c,d
   a,b,c         b,c,d
   a,b,c,d

"""

class Solution:
    def possibleSubstring(self,string):
        n = len(string)
        for i in range(n):
            for j in range(i,n):
                for k in range(i,j+1):
                    print(string[k],end=" ")
                print()
            print()

def main():
    string = input("Enter the string:")
    sol = Solution()

    sol.possibleSubstring(string)

if __name__ =="__main__":
    main()