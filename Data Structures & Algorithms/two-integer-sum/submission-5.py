class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Keep track of original indices because sorting loses them
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        indexed_nums.sort()
        
        l=0
        r=len(indexed_nums)-1

        while l<r:
            sum=indexed_nums[l][0]+indexed_nums[r][0]
            if sum==target:
                res = [indexed_nums[l][1], indexed_nums[r][1]]
                res.sort()
                return res
            elif sum<target:
                 l+=1
            else:
                r-=1
        return [-1,-1]