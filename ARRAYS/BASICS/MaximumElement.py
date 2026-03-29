

"""
 Given an array, we have to find the largest element in the array.

 constraints :
 1 <= arr.size()<= 10**6
 0 <= arr[i] <= 10**6
 or 
 -10**6 <=arr[i]<=10**6

 TC: O(N)
 SC:O(1)
"""

class Solution :
    def maximumElement(self,arr,maxele=None):
        if maxele is None:
            maxele = float('-inf')
        for ele in range(len(arr)):
            if arr[ele] > maxele :
                maxele = arr[ele]
        return maxele 
    
def main():
        print("enter the list size :")
        n = int(input())
        print("enter the elements of list ")
        l=list(map(int,input().split()))
        sol = Solution()
        result =sol.maximumElement(l)
        print(result)

    
if __name__ == "__main__":
    main()
    