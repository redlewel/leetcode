from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m <= 1:
            pass
        else:
            for i in range(0, n):
                self.merge_single(nums1, nums2)


    @staticmethod 
    def merge_single(nums1: List[int], nums2: List[int]):
        for i2, n2 in enumerate(nums2): 
            for i1, n1 in enumerate(nums1): 
                if n1 > n2:
                    print(f"Current Nums1: {nums1}")
                    step_place = i1 + 1
                    temp = n1
                    nums1[i1] = n2
                    if nums1[step_place] == 0: # If next index is 0 then jump to next n
                        nums1[step_place] = temp
                        continue
                    while nums1[step_place] != 0:
                        step_temp = nums1[step_place]
                        nums1[step_place] = temp
                        temp = step_temp
                        step_place += 1
                        



