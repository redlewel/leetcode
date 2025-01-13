
from typing import List

class Solution:
	def increasingTriplet(self, nums: List[int]) -> bool:
		for i in range(1, len(nums) - 1):
			if nums[i - 1] < nums[i] < nums[i + 1]:
				return True
			for j in range(i + 1, len(nums)):
				if nums[i] < nums[j]:
					for k in range(j + 1, len(nums)):
						print(f"""Index: i: {i}, j: {j}, k: {k}\n # <- shows how it passes testcase 62
								Values: i: {nums[i]}, j: {nums[j]}, k: {nums[k]}""")
						if nums[j] < nums[k]:
							return True
		return False

dog = Solution()
dog.increasingTriplet([1,2,1,3])

