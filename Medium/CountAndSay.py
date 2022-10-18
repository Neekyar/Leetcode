class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            return self.count(self.countAndSay(n-1))
        
    def count(self, s):
	    letter = s[0]
	    k = 1
	    res = ""
	    for char in s[1 : ]:
		    if char == letter:
			    k += 1
		    else:
			    res  = res + str(k) + letter
			    letter = char
			    k = 1
	    res = res + str(k) + letter
	    return res
            
