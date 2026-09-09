class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        loop = 0
        while loop < length:
            if nums[loop] == val:
                nums.pop(loop)
                length -= 1
            else:
                loop += 1
        return length
        