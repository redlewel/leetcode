from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m <= 1:
            pass
        for i in range(0, n):
            print(f"Main loop of {i}")
            for i1, n1 in enumerate(nums1):
                if nums2[i] < n1:
                    step = nums2[i]
                    index1 = i1
                    print(f"For: step: {step}, index1: {index1}\nNums1: {nums1} ")
                    while nums1[index1 + 1] != 0:
                        temp = nums1[index1]
                        nums1[index1] = step
                        step = nums1[index1 + 1]
                        nums1[index1 + 1] = temp
                        index1 += 1

                    print(f"While print\nindex1: {index1} ,step: {step}")
                        


