"""
OK, so this is using something called prefix product arrays: https://www.geeksforgeeks.org/prefix-product-array/
and https://www.geeksforgeeks.org/suffix-product-array/

seems according to this video: https://www.youtube.com/watch?v=5bS636lE_R0
Its more like right and left not exactly full prefix and full suffix.  So I need to remove the first calc on each side. 

"""
from typing import List
class Solution:
    def suffix(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suffix_product = [1] * n

        for i in range(n - 2, -1, -1):
            suffix_product[i] = suffix_product[i + 1] * nums[i + 1]
        return suffix_product

    def prefix(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i] * nums[i - 1]
        return nums

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix_arr = self.suffix(nums)
        prefix_arr = self.prefix(nums)
        for i in range(len(nums)): 
            nums[i] = suffix_arr[i] * prefix_arr[i]
        return nums


dog = Solution()
#print(dog.productExceptSelf([1,2,3,4]))
print(dog.prefix([1,2,3,4]))
print(dog.suffix([1,2,3,4]))

#dog.productExceptSelf([-1,1,0,-3,3])


