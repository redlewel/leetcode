from typing import List

class Solution:
	def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
		if len(nums1) < 2:
			if nums1[0] == 0:
				nums1[0] = nums2[0]
		if len(nums1) < 3:
			if nums1[1] == 0:
				nums1[1] = nums2[0]
		place = len(nums1) - 1
		for i in range(0, n):
			for a in range(place, 0, -1):
				if nums1[a] == 0:
					continue
				if nums2[i] >= nums1[a]:
					print(f"List before: {nums1}")
					print(f"nums2[i]: {nums2[i]}, nums1[a]: {nums1[a]}")
					nums1.insert(a + 1, nums2[i])
					place = a + 1
					nums1.pop()
					print(f"List after: {nums1}")
					break
		print(nums1)

solve = Solution()
solve.merge([1, 2, 4, 0, 0, 0], 3, [2, 5, 6], 3)
solve.merge([1, 0], 1, [2], 1)

