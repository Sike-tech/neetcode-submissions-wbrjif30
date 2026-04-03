class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
            '''
            nums = [2,7,11,5]; target = 13
            complement = 13-2 = 11
            seen = {2:0}

            complement = 13-7 = 6
            # complement is not in seen
            seen = {2:0,7:1}

            complement = 13-11 = 2
            #complement is in seen
            True is returned

            * we are checking if the diffence of the target and number is present
            in seen because that diffence + the number = target
            '''