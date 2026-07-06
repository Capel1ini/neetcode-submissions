class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        target1 = {}
        for i in range(len(numbers)): 
            remaining = target - numbers[i]
            if remaining in target1: 
                return [target1[remaining]+1, i+1]
            else: 
                target1[numbers[i]] = i 
                
        