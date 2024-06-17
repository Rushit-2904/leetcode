from typing import List

class Solution:
    def merge(self, a: List[int], m: int, b: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j,k = m-1,n-1,len(a)-1
        while i>=0 and j>=0:
            if a[i]>b[j]:
                a[k] = a[i]
                i -= 1
            else:
                a[k] = b[j]
                j -= 1
            k -= 1
        while i>=0:
            a[k] = a[i]
            i -= 1
            k -= 1
        while j>=0:
            a[k] = b[j]
            j -= 1
            k -= 1