class Solution:
    def maximum69Number (self, num: int) -> int:
        s = list(str(num))
        if '6' not in s: return num
        s[s.index('6')] = '9'
        return ''.join(s)
        
