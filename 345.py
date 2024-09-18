class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'auieoAEIOU'
        vowel_list = []
        for i in enumerate(s):
            if i[1] in vowels:
                vowel_list.append(i[1])
        newstr = ''
        for i in s:
            if i in vowels:
                newstr = newstr + vowel_list.pop()
            else:
                newstr = newstr + i
                
        return newstr
