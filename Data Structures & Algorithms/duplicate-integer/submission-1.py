class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d={}
        for i in nums:
            if i in d:
                return True
            else:
                d[i]=1
        return False
        '''
        for j in d:
            if d[j]>=2:
                return True
        return False
        '''

            


'''
            i=1,2,3,3
            i=1   d={1:1}
            i=2   d={1:1,2:1}
            i=3   d={1:1,2:1,3:1}
            i=3   d={1:1,2:1,3:2}
            '''


        