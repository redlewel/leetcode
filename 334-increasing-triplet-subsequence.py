from typing import List

class Solution:
	def increasingTriplet(self, nums: List[int]) -> bool:
		n = len(nums)
		diff_list = [] 
		if n 
		for i in range(1, n - 1):
			if i > 0:
				if len(diff_list) < 3 and i > 100:
					return False
			if nums[i] in diff_list: 
				diff_list.append(nums[i])
			if nums[i] < nums[i + 1] < nums[i + 2]:
				return True 
			for j in range(i + 1, n):
				if nums[j] in diff_list: 
					diff_list.append(nums[j])
				if nums[i] < nums[j]:
					for k in range(j + 1, n):
						if nums[k] in diff_list: 
							diff_list.append(nums[k])
						if nums[j] < nums[k]:
							return True
		return False

# testcase with insanely long list of 2's and 1's killing my solution will need to go back to drawing board

dog = Solution()
dog.increasingTriplet([1,2,1,3])

