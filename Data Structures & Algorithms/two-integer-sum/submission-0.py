class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index_dict={}
        for index,num in enumerate(nums):
            x=target-num
            if x in num_index_dict:
                return [num_index_dict[x],index]
            num_index_dict[num]=index


             