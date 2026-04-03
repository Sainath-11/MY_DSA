"""
Union of Two Sorted Arrays

Problem Statement: Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.

The union of two arrays can be defined as the common and distinct elements in the two arrays.

NOTE: Elements in the union should be in ascending order.

Examples

Input:n = 5,m = 5 arr1[] = {1,2,3,4,5}  arr2[] = {2,3,4,4,5}
Output: {1,2,3,4,5}
Explanation: Common Elements in arr1 and arr2  are:  2,3,4,5
Distnict Elements in arr1 are : 1
Distnict Elemennts in arr2 are : No distinct elements.
Union of arr1 and arr2 is {1,2,3,4,5}

Input:n = 10,m = 7,arr1[] = {1,2,3,4,5,6,7,8,9,10}arr2[] = {2,3,4,4,5,11,12}
Output: {1,2,3,4,5,6,7,8,9,10,11,12}
Explanation: Common Elements in arr1 and arr2  are:  2,3,4,5
Distnict Elements in arr1 are : 1,6,7,8,9,10
Distnict Elemennts in arr2 are : 11,12
Union of arr1 and arr2 is {1,2,3,4,5,6,7,8,9,10,11,12}

1  ≤  a.size(), b.size()  ≤  10**5
-10**9 ≤ a[i], b[i] ≤10** 9

"""

class Solution:
    def HashMapMethod(self,a,b):
        # TC : (NLOGN+N) SC:0(N) 
        d={}
        for i in range(len(a)):
            if a[i] in d:
                d[a[i]]=d[a[i]]+1
            else:
                d[a[i]]=1
        # print(d)
        for i in range(len(b)):
            if b[i] in d:
                d[b[i]] = d[b[i]]+1
            else:
                d[b[i]]=1
        ans=list()
        for i in sorted(d):
            ans.append(i)
        return ans
                
    def SetMethod(self,a,b):
        #TC:0(N+NLOGN) SC:O(N)
        for i in range(len(b)):
            a.append(b[i])
        # print(set(a))
        return sorted(list(set(a)))
        # ans=list()
    
    def TwoPointersApproach(self,a,b):
        #TC:O(N+M) SC:0(N+M)
        r=list()
        i,j = 0 ,0 
        n ,m = len(a),len(b)
        
        while i< n and j < m :
            if a[i] < b[j]:
                if len(r)==0 or r[-1]!=a[i]:
                    r.append(a[i])
                i = i +1
            elif a[i] > b[j] :
                if len(r)==0 or r[-1]!=b[j]:
                    r.append(b[j])
                j = j + 1 
            else:
                if len(r)==0 or r[-1]!=a[i]:
                    r.append(a[i])
                i = i +1
                j = j +1
        
        while i< n :
            if len(r)==0 or r[-1]!=a[i]:
                r.append(a[i])
            i = i +1 
        while j < m:
            if len(r)==0 or r[-1]!=b[j]:
                r.append(b[j])
            j = j + 1 
        return r    
                
def main():
    n ,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int , input().split()))
    sol = Solution()
    print(sol.TwoPointersApproach(a,b)) 

if __name__ == "__main__":
    main()
