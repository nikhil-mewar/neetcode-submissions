class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        b=[]
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in a:
                a[nums[i]]=i
            else :
                b.append(a[complement])
                b.append(i)
        return b
        