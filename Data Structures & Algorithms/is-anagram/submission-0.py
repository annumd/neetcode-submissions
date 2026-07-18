class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):  #length saame aanonn nokki egs: abcd efgh
            return False
        count_s={} #racecar
        count_t={}
        for ch in s: #count ondaaki for s
            if ch in count_s:
                count_s[ch]+=1
            else:
                count_s[ch]=1
        for ch in t: #count  ondaaki for t
            if ch in count_t:
                count_t[ch]+=1
            else:
                count_t[ch]=1

        for key in count_s: #goes thru each letter in count_s
            if key not in count_t:  #if that letter not in count_s
                return False
            if count_s[key] != count_t[key]: 
                #if letter is there(bcs for 'FOR KEY IN COUNT_S') but count is different
                return False  
        return True







            
                