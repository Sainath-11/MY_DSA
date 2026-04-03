"""Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 10**4
-2**31 <= nums[i] <= 2**31 - 1
"""

class Soultion:
    def MoveZeros(self,arr):
        left= 0 
        for right in range(len(arr)):
            if arr[right]!=0:
                arr[left],arr[right] = arr[right],arr[left]
                left = left + 1
def main():
    n = int(input("Enter the size of array:"))
    l=list(map(int,input("Enter the element of array:").split()))
    sol = Soultion()
    sol.MoveZeros(l)
    print(l)
if __name__ =="__main__":
    main()


        


