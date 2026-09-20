class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        index1 = m - 1
        index2 = n - 1
        slot = len(nums1) - 1
        while (index2 >= 0 and index1 >= 0):
            if nums1[index1] >= nums2[index2]:
                nums1[slot] = nums1[index1]
                index1 -= 1
                slot -= 1
            else:
                nums1[slot] = nums2[index2]
                index2 -= 1
                slot -= 1
        if index2 >= 0:
            for x in range(0, index2 + 1):
                nums1[x] = nums2[x]
            
            
    
                



            


        