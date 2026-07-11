class Solution:
    def isPalindrome(self, s: str) -> bool:
        word=""
        for ch in s:
            if ch.isalnum():
                word+=ch.lower()
            else:
                continue
        pal=word[::-1]
        return word==pal
          