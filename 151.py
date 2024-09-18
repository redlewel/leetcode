class Solution: 
	def reverseWords(self, s: str) -> str:
		reversed_word = s.split(" ")
		non_space_list = []
		for r in reversed_word: 
			if r != '' and r != " ":
				non_space_list.append(r)
		reverse = non_space_list.pop()
		for r in reversed(non_space_list):
			reverse = reverse + " " + r
		return reverse

