# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i,j = 1,n
        
        while i<j:
            pivot = (i+j)//2
            if isBadVersion(pivot):
                j = pivot #Track the leftmost bad version
            else:
                i = pivot + 1 #Track the rightmost good version
        return i
        
        
