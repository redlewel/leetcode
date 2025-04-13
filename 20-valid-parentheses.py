class Solution:		
	def isValid(self, s: str) -> bool:
		curl_stack = []
		try:
			for char in s:
				if char == "{" or char == "[" or char == "(":
					curl_stack.append(char)
				if char == "}":
					if curl_stack.pop() != "{":
						return False
				elif char == "]":
					if curl_stack.pop() != "[":
						return False
				elif char == ")":
					if curl_stack.pop() != "(":
						return False
		except IndexError:
			return False
		if len(curl_stack) == 0:
			return True
		else: 
			return False

				

				
				
		
