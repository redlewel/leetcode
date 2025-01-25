from typing import List

class Solution:
	def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
		place = 0
		for i in range(0, n):
			print("dog")
			for a in range((len(nums1) - 1), 0, -1):
				print("cat")
				if nums1[a] == 0:
					continue
				if nums2[i] >= nums1[a]:
					print(f"current list: {nums1}")
					print(f"Nums2[i]: {nums2[i]} Nums1[a]: {nums1[a]}")
					nums1.insert(a + 1, nums2[i])
					place = i + 1
					nums1.pop()
					print(f"list after: {nums1}")
					break
		print(nums1)

solve = Solution()
solve.merge([1, 2, 4, 0, 0, 0], 3, [2, 5, 6], 3)

