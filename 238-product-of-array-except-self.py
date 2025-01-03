"""
OK, so this is using something called prefix product arrays: https://www.geeksforgeeks.org/prefix-product-array/
and https://www.geeksforgeeks.org/suffix-product-array/

seems according to this video: https://www.youtube.com/watch?v=5bS636lE_R0
Its more like right and left not exactly full prefix and full suffix.  So I need to remove the first calc on each side. 

Figured it out.  So what was needed is to multiply on the same level on each side.  This is because it's needed to keep in mind that the input 
and prefix/suffix arrays are still different, so you multiply at the same index to get the result of the following or preceding index when populating
the prefix and suffix arrays. That's something that tripped me up.  
Because this is all the left side and right sides multiplied when multiplying across you multiply everything in the array minus the actual value at 
that index, because that is not included when multiplying from only left or right.  The video explains this more thoroughly. 

"""
from typing import List
class Solution:

    def prefix(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_product = [1] * n
        for i in range(1, n):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1] 
        return prefix_product

    def suffix(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suffix_product = [1] * n
        for i in range(n - 2, -1, -1):
            suffix_product[i] = suffix_product[i + 1] * nums[i + 1]
        return suffix_product

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix_arr = self.suffix(nums)
        prefix_arr = self.prefix(nums)
        for i in range(len(nums)): 
            nums[i] = suffix_arr[i] * prefix_arr[i]
        return nums


dog = Solution()
print(dog.productExceptSelf([1,2,3,4]))
print(dog.prefix([1,2,3,4])) # This should be [1, 1, 2, 6]
print(dog.suffix([1,2,3,4])) # This should be [24,12, 4, 1]

#dog.productExceptSelf([-1,1,0,-3,3])


