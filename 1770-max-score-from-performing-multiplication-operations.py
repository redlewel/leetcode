class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        score = 0
        for m in multipliers:
            print(f"M value: {m} | Nums: {nums}")
            score += self.establish_polarity(nums, m)
            print(f"Total score: {score}")
        return score
            
    def establish_polarity(self, nums, m):
        # Start + m is positive result
        pos_start = nums[0] > 0
        pos_end = nums[-1] > 0
        neg_start = nums[0] < 0
        neg_end = nums[-1] < 0 
        self.marker = {nums[0]: 'start', nums[-1]: 'end'}
        if m > 0:   
            if pos_start or pos_end:
                # we use absolute value to get the largest number for result
                return self.calc_max(nums, m)
            else:
                return self.calc_min(nums, m, True) 
        elif m < 0:
            if neg_start or neg_end:
                return self.calc_max(nums, m, True)
            else: 
                return self.calc_min(nums, m, True)

    def calc_min(self, nums, m, absolute=False): 
        if absolute:
            result = min(nums[0], nums[-1], key=abs)
        else:
            result = min(nums[0], nums[-1])
        self.mark = self.marker[result]
        self.shrink_array(nums)
        print(f'Positive, Result: {result * m}')
        return m * result 

    def calc_max(self, nums, m, absolute=False): 
        if absolute:
            result = max(nums[0], nums[-1], key=abs)
        else:
            result = max(nums[0], nums[-1])
        self.mark = self.marker[result]
        self.shrink_array(nums)
        print(f'Positive, Result: {result * m}')
        return m * result 
    
    def shrink_array(self, nums): 
        # del is used below since we want to modify original list, not create a copy
        if self.mark == 'end': 
            del nums[-1]
        elif self.mark == 'start': 
            del nums[0]
        else: 
            raise ValueError("incorrect value!")

# THIS NEEDS DYNAMIC PROGRAMMING...........   GONNA HAVE TO REVISIT
