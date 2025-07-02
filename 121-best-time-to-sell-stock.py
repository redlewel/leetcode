class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newNums = nums
        for bindex, base in enumerate(nums): 
            print(f"Base {base}")
            newNums = newNums[1:]
            for aindex, add in enumerate(newNums):
                print(f"Add {add}")
                if base + add == target:
                    offset_index = self.calc_offset(len(nums), len(newNums), aindex)
                    return [bindex, offset_index]
                
    def calc_offset(self, nums_len, newnums_len, aindex):
        offset = nums_len - newnums_len 
        return offset + aindex
