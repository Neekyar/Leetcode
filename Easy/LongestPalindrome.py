class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash = set()
        for letter in s:
            if letter not in hash:
                hash.add(letter)
            else:
                hash.remove(letter)
        
        # hash count is the number of odd letters
        return len(s) - len(hash) + 1 if len(hash) > 0 else len(s)