class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        set_list = {}
        for s in strs:
            word_set = self.destruct(s)
            print(word_set)
            if word_set not in set_list:
                set_list[word_set] = [s]
            else:
                set_list[word_set].append(s)
        for sets in set_list.values():
            anagrams.append(sets)
        return anagrams    

    def destruct(self, word):
        word_list = sorted(word)
        new_word = ""
        for w in word_list:
            new_word += w 
        return new_word
    
