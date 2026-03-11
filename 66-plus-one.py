class Solution:
	def plusOne(self, digits: List[int]) -> List[int]:
		num_str = ''
		for i in digits:
			num_str += str(i)
		number = int(num_str) + 1
		num_str = str(number)
		num_arr = []
		for s in num_str:
			num_arr.append(int(s))
		return(num_arr)
