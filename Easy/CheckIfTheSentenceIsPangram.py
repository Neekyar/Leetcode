class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        check = [0] * 26
        for letter in sentence:
            check[ord(letter) % 97] = 1
        for i in range(26):
            if check[i] == 0:
                return False
        return True
