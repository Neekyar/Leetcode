class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        res = ''
        i,j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            carry += int(a[i]) if i >= 0 else 0
            carry += int(b[j]) if j >= 0 else 0
            res = str(carry % 2) + res
            carry //= 2
            i,j = i-1, j-1
        return res
            