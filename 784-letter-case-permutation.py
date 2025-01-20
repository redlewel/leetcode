"""
Thinking, this is a permutation and the only ones that change are letters.
permutation is factorial.  I am thinking this needs recursion. 


"""
from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        letterIndices = self.findLetterIndices(s)
        limit = factNum(len(letterIndices))
        return recurseIndices(s, letterIndices, limit)
                
    def recurseIndices(s: str, indices: List[int], limit: int, stringList: List[str] = [], count: int = 0) -> List[str]:
        # BASE CASE
        if count == limit:
            return stringList
        else:
            count += 1
        return # not sure on this need to come back with fresh set of eyes

    def factorial(num: int) -> int:
        factNum = 1
        for n in range(num, -1, 0):
            factNum = factNum * n
        return factNum





    def findLetterIndices(self, s: str) -> List[int]:
        letterIndices = []
        for letter in s:
            if letter.isalpha():
                letterIndices.append(s.index(letter))
        return letterIndices

