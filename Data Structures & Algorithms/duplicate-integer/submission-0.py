class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        output = False
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i != j:
                    output = True
                    break
                else:
                    output = False
            if output == True:
                break
        return output