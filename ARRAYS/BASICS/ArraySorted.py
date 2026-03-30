"""
1)Given an array of size n, write a program to check if the given array is sorted 
in (ascending / Increasing(means no duplaicates be ) / Non-decreasing(array may be constant or striclty increasing)) order or not. 
If the array is sorted then return True, Else return False.

arr=[1,2,2,2] -- > Non decreasing + increasing 
arr=[1,2,4,6] -- > ascedning / increasing 


                                              [or]
                                        
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). 
Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.


"""
class Solution :
    def isSorted(self,arr)->bool:
        for i in range(1,len(arr)):
            if arr[i-1]>arr[i]:
                return False
        return True
    def checkRotatedSorted(self,arr)->bool:
        # rember and rotated sorted array : propteries 
        # 1) arr[firstele] >= arr[lastele] 
        # 2) definetly have peak point --> which says no of times its rotated 
        # [3,6,9,10] --> [10,3,6,9] x=1 (index)--> [9,10,3,6] (x=2)--> [6,9,10,3](x=3) --> [3,6,9,10]
        count = 0 
        for i in range(len(arr)):
            if arr[i-1]>arr[i]:
                count = count +1
        if count <=1:
            return True 
        return False
def main():
    n = int(input("enter the size of array :"))
    l = list(map(int , input("enter the elements of array :").split()))
    sol = Solution()
    print(sol.isSorted(l))
    print(sol.checkRotatedSorted(l))

if __name__ == "__main__":
    main()
