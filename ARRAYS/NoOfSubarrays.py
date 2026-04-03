"""
Genrate the number of subarrays 
arr=[1,2,3,4]

subarrays: o((n*(n+1))//2)
   1             2         3          4 
   1,2           2,3       3,4
   1,2,3         2,3,4
   1,2,3,4

"""

class Solution:
    def possibleSubarrays(self,arr):
        n = len(arr)
        for i in range(n):
            for j in range(i,n):
                for k in range(i,j+1):
                    print(arr[k],end=" ")
                print()
            print()
    

def main():
    n = int(input("Enter the size of array:"))
    l = list(map(int, input("Enter the element of array:").split()))
    sol = Solution()

    sol.possibleSubarrays(l)

if __name__ =="__main__":
    main()
    


